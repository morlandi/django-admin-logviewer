import os
import glob
import hashlib
from django.shortcuts import render
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .app_settings import LOGS, REFRESH_INTERVAL, INITIAL_NUMBER_OF_CHARS


def logs(as_list):
    """
    Get the list of all log paths;
    for each path we also calculate a checksum for later lookup;
    we do not rely on path positions, since new paths can come an go at any time

    Either return:

        [{
            'checksum': '37bf7627035ca1dc719c9d8c3d1b56c7',
            'path': '/whatever/logs/aaa.log'
        }, {
            'checksum': 'ea5dc95db52ff1d1cb45127605a34cf6',
            'path': '/whatever/logs/bbb.log'},
            ...
        }]

    or, for faster lookup:

        {
            '37bf7627035ca1dc719c9d8c3d1b56c7': '/whatever/logs/aaa.log',
            'ea5dc95db52ff1d1cb45127605a34cf6': '/whatever/logs/bbb.log',
            ...
        }

    """

    filenames = [] if as_list else {}

    def append_path(path):

        # Fix for Windows
        path = path.replace('\\', '/')

        checksum = hashlib.md5(path.encode()).hexdigest()
        if as_list:
            filenames.append({
                'path': path,
                'checksum': checksum,
            })
        else:
            filenames[checksum] = path

    for log in LOGS:
        paths = sorted(glob.glob(log))
        if not paths:
            # file does not exist; we still append the path
            append_path(log)
        else:
            for path in paths:
                append_path(path)

    return filenames


@staff_member_required
def view_logs(request):

    return render(request, 'logviewer/logs.html', {
        'logs': logs(as_list=True),
        'refresh_interval': REFRESH_INTERVAL,
    })


@staff_member_required
def get_log_lines(request, log_id):

    last_position = int(request.GET.get('last_position', 0))
    response = {
        'last_position': 0,
        'content': []
    }

    try:
        path = logs(as_list=False)[log_id]
        with open(path, 'r') as file:

            # file.seek(0, os.SEEK_END)
            # if last_position and last_position <= file.tell():
            #     file.seek(last_position)

            if last_position <= 0:
                # The very first time, let's read the last INITIAL_NUMBER_OF_CHARS bytes
                file.seek(0, os.SEEK_END)
                position = max(0, file.tell() - INITIAL_NUMBER_OF_CHARS)
                file.seek(position)
            else:
                # let's pick up where we left off
                file.seek(0, os.SEEK_END)
                if last_position <= file.tell():
                    file.seek(last_position)

            for line in file:
                response['content'].append('%s' % line.replace('\n','<br/>'))
            response['last_position'] = file.tell()
        return JsonResponse(response)
    except Exception as e:
        return JsonResponse(str(e), status=400, safe=False)

@staff_member_required
def download(request, log_id):
    try:
        path = logs(as_list=False)[log_id]
        with open(path, 'r') as file:
            buffer = file.read()
        response = HttpResponse(buffer, content_type='plain/text')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.split(path)[1]
    except Exception as e:
        messages.error(request, str(e))
        response = HttpResponseRedirect(reverse('logviewer:logs'))
    return response

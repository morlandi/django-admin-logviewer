import os
from django.shortcuts import render
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .app_settings import LOGS, REFRESH_INTERVAL


@staff_member_required
def view_logs(request):

    return render(request, 'logviewer/logs.html', {
        'logs': LOGS,
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
        with open(LOGS[log_id], 'r') as file:
            file.seek(0, os.SEEK_END)
            if last_position and last_position <= file.tell():
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
        path = LOGS[log_id]
        with open(LOGS[log_id], 'r') as file:
            buffer = file.read()
        response = HttpResponse(buffer, content_type='plain/text')
        response['Content-Disposition'] = 'attachment; filename=%s' % os.path.split(path)[1]
    except Exception as e:
        messages.error(request, str(e))
        response = HttpResponseRedirect(reverse('logviewer:logs'))
    return response

from django.shortcuts import render
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from pathlib import Path
from .app_settings import LOGS


@staff_member_required
def view_logs(request):

    logs = [{
        'name':  Path(log).name,
        'path': log,
    } for log in LOGS ]

    return render(request, 'logviewer/logs.html', {
        'logs': logs,
    })

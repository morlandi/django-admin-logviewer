from django.shortcuts import render
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from .app_settings import LOGS


@staff_member_required
def view_logs(request):

    return render(request, 'logviewer/logs.html', {
        'logs': LOGS,
    })

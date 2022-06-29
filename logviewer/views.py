from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def view_logs(request):
    return render(request, 'logviewer/logs.html', {
    })

from django.urls import path
from . import views

app_name = "logviewer"


urlpatterns = [
    path('logs/', views.view_logs, name='logs'),
    #path('get-log-line/<int:file_id>/', views.get_log_lines, name='logtailer_get_log_lines'),
]

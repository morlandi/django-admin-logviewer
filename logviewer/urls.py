from django.urls import path
from . import views

app_name = "logviewer"


urlpatterns = [
    path('logs/', views.view_logs, name='logs'),
    path('get_log_lines/<str:log_id>/', views.get_log_lines, name='get_log_lines'),
    path('download/<str:log_id>/', views.download, name='download'),
]

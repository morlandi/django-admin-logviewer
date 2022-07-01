from django.conf import settings

LOGS = getattr(settings, 'LOGVIEWER_LOGS', [])
REFRESH_INTERVAL = getattr(settings, 'LOGVIEWER_REFRESH_INTERVAL', 1000)

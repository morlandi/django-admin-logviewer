from django.conf import settings

LOGS = getattr(settings, 'LOGVIEWER_LOGS', [])

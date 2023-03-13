from django.conf import settings

LOGS = getattr(settings, 'LOGVIEWER_LOGS', [])
REFRESH_INTERVAL = getattr(settings, 'LOGVIEWER_REFRESH_INTERVAL', 1000)
INITIAL_NUMBER_OF_CHARS = getattr(settings, 'LOGVIEWER_INITIAL_NUMBER_OF_CHARS', 2048)

import os
from app.settings import DEBUG
from django.core.wsgi import get_wsgi_application

if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.production")

application = get_wsgi_application()

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gold_diary_svc.settings")

application = get_wsgi_application()

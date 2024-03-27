import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gold_diary_svc.settings.prod")

application = get_asgi_application()

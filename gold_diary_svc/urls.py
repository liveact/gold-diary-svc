from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("api_auth/", include("rest_framework.urls")),
    path("api/gold/", include("apps.gold.urls", namespace="gold")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

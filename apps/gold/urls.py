from django.urls import path

from apps.gold.views import GoldListCreateAPIView, GoldDetailAPIView

app_name = "gold"
urlpatterns = [
    path("", GoldListCreateAPIView.as_view(), name="gold_list_create_api"),
    path("<int:pk>/", GoldDetailAPIView.as_view(), name="gold_detail_api"),
]

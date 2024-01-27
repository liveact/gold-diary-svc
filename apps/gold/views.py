from rest_framework import generics

from apps.gold.models import Gold
from apps.gold.serializers import GoldSerializer
from apps.utils.response import CreateResponseMixin, RetrieveUpdateDeleteResponseMixin


class GoldListCreateAPIView(CreateResponseMixin, generics.ListCreateAPIView):
    serializer_class = GoldSerializer

    def get_queryset(self):
        return Gold.objects.filter(user_id=self.request.user.id)


class GoldDetailAPIView(
    RetrieveUpdateDeleteResponseMixin, generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = GoldSerializer

    def get_queryset(self):
        return Gold.objects.filter(user_id=self.request.user.id)

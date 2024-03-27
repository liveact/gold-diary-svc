from rest_framework import generics

from apps.utils.serializers import LoginSerializer


class LoginAPIView(generics.CreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = LoginSerializer

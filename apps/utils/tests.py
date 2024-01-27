from django.contrib.auth.models import User
from rest_framework.test import APITestCase


class BaseAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.test_user = User.objects.create_user(
            username="username", password="password"
        )
        self.client.login(username=self.test_user.username, password="password")

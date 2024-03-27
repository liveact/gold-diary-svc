import json

from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class BaseAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.test_user = User.objects.create_user(
            username="username", password="password"
        )
        self.test_user.set_password("password")
        self.test_user.save()
        self.client.login(username=self.test_user.username, password="password")

    def test_login(self):
        response = self.client.post(
            reverse("login"),
            data=json.dumps({"username": "username", "password": "password"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)

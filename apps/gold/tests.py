from rest_framework import status
from rest_framework.reverse import reverse

from apps.gold.models import Gold
from apps.utils.tests import BaseAPITestCase


class GoldTest(BaseAPITestCase):
    def test_create_gold(self):
        self.assertEqual(Gold.objects.count(), 0)
        response = self.client.post(reverse("gold:gold_list_create_api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Gold.objects.count(), 1)

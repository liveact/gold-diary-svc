import json

from rest_framework import status
from rest_framework.reverse import reverse

from apps.gold.models import Gold
from apps.utils.tests import BaseAPITestCase


class GoldTest(BaseAPITestCase):
    def setUp(self) -> None:
        super().setUp()
        self.assertEqual(Gold.objects.count(), 0)
        self.gold = Gold.objects.create(
            name="initial_gold",
            label_weight=1.21,
            total_price=450,
            buy_time="2021-01-01 00:00:00",
            buy_channel="JD",
            remark="备注",
            actual_weight=1.28,
            user=self.test_user,
        )

    def test_create_gold(self):
        data = {
            "name": "gold",
            "label_weight": "1.21",
            "total_price": "450",
            "buy_time": "2021-01-01 00:00:00",
            "buy_channel": "TB",
            "remark": "备注",
            "actual_weight": "1.28",
        }
        response = self.client.post(
            reverse("gold:gold_list_create_api"),
            data=json.dumps(data),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json()["data"]["results"][0]
        self.assertEqual(result["name"], data["name"])
        self.assertEqual(result["label_weight"], "1.210")
        self.assertEqual(result["total_price"], "450.00")
        self.assertEqual(result["buy_channel"], data["buy_channel"])
        self.assertEqual(result["remark"], data["remark"])
        self.assertEqual(result["actual_weight"], "1.280")
        self.assertEqual(result["real_univalent"], "351.56")
        self.assertEqual(result["label_univalent"], "371.90")

    def test_patch_gold(self):
        data = {
            "name": "update_gold",
            "label_weight": "1.25",
            "total_price": "480",
            "actual_weight": "1.28",
        }

        response = self.client.patch(
            reverse("gold:gold_detail_api", kwargs={"pk": self.gold.id}),
            data=json.dumps(data),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json()["data"]["results"][0]
        self.assertEqual(result["name"], data["name"])
        self.assertEqual(result["label_weight"], "1.250")
        self.assertEqual(result["total_price"], "480.00")
        self.assertEqual(result["real_univalent"], "375.00")
        self.assertEqual(result["label_univalent"], "384.00")

    def test_delete_gold(self):
        self.assertEqual(Gold.objects.count(), 1)
        response = self.client.delete(
            reverse("gold:gold_detail_api", kwargs={"pk": self.gold.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["data"]["results"], [])
        self.assertEqual(Gold.objects.count(), 0)
        self.assertEqual(Gold.all_objects.count(), 1)

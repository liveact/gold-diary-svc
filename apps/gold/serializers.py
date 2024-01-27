from rest_framework import serializers

from apps.gold.models import Gold
from apps.utils.serializers import SetUserSerializerMixin


class GoldSerializer(SetUserSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Gold
        fields = [
            "name",
            "label_weight",
            "total_price",
            "buy_time",
            "channel",
            "remark",
            "actual_weight",
            "univalent",
            "crit",
        ]

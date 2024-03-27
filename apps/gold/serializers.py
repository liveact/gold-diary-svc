from rest_framework import serializers

from apps.gold.models import Gold
from apps.utils.serializers import SetUserSerializerMixin


class GoldSerializer(SetUserSerializerMixin, serializers.ModelSerializer):
    real_univalent = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True
    )
    label_univalent = serializers.DecimalField(
        max_digits=12, decimal_places=2, read_only=True
    )
    crit = serializers.DecimalField(max_digits=12, decimal_places=3, read_only=True)

    class Meta:
        model = Gold
        fields = [
            "name",
            "label_weight",
            "total_price",
            "buy_time",
            "buy_channel",
            "remark",
            "actual_weight",
            "real_univalent",
            "crit",
            "label_univalent",
        ]

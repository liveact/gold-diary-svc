from django.contrib.auth.models import User
from django.db import models
from django.db.models import F
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Gold(SoftDeletableModel, TimeStampedModel):
    name = models.CharField(max_length=16, null=True, blank=True, help_text="名称")
    label_weight = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True, help_text="标签重量"
    )
    total_price = models.DecimalField(
        max_digits=12, decimal_places=2, null=True, blank=True, help_text="总价"
    )

    buy_time = models.DateTimeField(null=True, blank=True, help_text="购买时间")
    buy_channel = models.CharField(null=True, blank=True, max_length=32, help_text="渠道")
    remark = models.CharField(null=True, blank=True, max_length=255, help_text="备注")

    actual_weight = models.DecimalField(
        max_digits=12, decimal_places=3, null=True, blank=True, help_text="实际重量"
    )

    actual_univalent = models.GeneratedField(
        expression=F("total_price") / F("actual_weight"),
        output_field=models.DecimalField(
            max_digits=12, decimal_places=2, null=True, blank=True
        ),
        db_persist=True,
        null=True,
        blank=True,
    )

    label_univalent = models.GeneratedField(
        expression=F("total_price") / F("label_weight"),
        output_field=models.DecimalField(
            max_digits=12, decimal_places=2, null=True, blank=True
        ),
        db_persist=True,
        null=True,
        blank=True,
    )

    crit = models.GeneratedField(
        expression=F("actual_weight") - F("label_weight"),
        output_field=models.DecimalField(
            max_digits=12, decimal_places=3, null=True, blank=True
        ),
        db_persist=True,
        null=True,
        blank=True,
    )

    user = models.ForeignKey(User, related_name="golds", on_delete=models.DO_NOTHING)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name}-{self.buy_channel}"

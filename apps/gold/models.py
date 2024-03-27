from django.contrib.auth.models import User
from django.db import models
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
    user = models.ForeignKey(User, related_name="golds", on_delete=models.DO_NOTHING)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name}-{self.buy_channel}"

    @property
    def real_univalent(self):
        # 实际单价
        if self.total_price and self.actual_weight:
            return self.total_price / self.actual_weight

    @property
    def crit(self):
        # 暴击
        if self.actual_weight and self.label_weight:
            return self.actual_weight - self.label_weight

    @property
    def label_univalent(self):
        # 标签单价
        if self.total_price and self.label_weight:
            return self.total_price / self.label_weight

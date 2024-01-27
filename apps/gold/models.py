from django.contrib.auth.models import User
from django.db import models
from model_utils.models import TimeStampedModel


class Gold(TimeStampedModel):
    # g = label_weight * 1000
    # 元 = total_price * 100
    name = models.CharField(max_length=16, null=True, blank=True, help_text="商品名称")
    label_weight = models.IntegerField(null=True, blank=True, help_text="标签重量")
    total_price = models.IntegerField(null=True, blank=True, help_text="总价")

    buy_time = models.DateTimeField(null=True, blank=True, help_text="购买时间")
    channel = models.CharField(null=True, blank=True, max_length=32, help_text="渠道")
    remark = models.CharField(null=True, blank=True, max_length=32, help_text="备注")

    actual_weight = models.IntegerField(null=True, blank=True, help_text="实际重量")
    user = models.ForeignKey(User, related_name="golds", on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name}-{self.channel}"

    @property
    def univalent(self):
        # 实际单价
        if self.total_price and self.actual_weight:
            return self.total_price / self.actual_weight
        if self.total_price and self.label_weight:
            return self.total_price / self.label_weight

    @property
    def crit(self):
        # 暴击
        if self.actual_weight and self.label_weight:
            return self.actual_weight - self.label_weight

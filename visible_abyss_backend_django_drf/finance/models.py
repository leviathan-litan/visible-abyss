from django.db import models
from django.contrib.auth.models import User

from account.models import *
from tag.models import *

# Create your models here.

class Charge(models.Model):

    created_at = models.DateField(
        verbose_name="发生时间",
        # auto_now_add=True,
        # auto_now=True,
        auto_created=True,
        editable=True,
    )
    matter = models.CharField(
        verbose_name="事件名",
        max_length=200,
    )

    # 「支出」与「收入」两方均为自然人
    # 在不同的经济活动中，它们可能同时存在，也可能只存在其中一方
    expend_side = models.ForeignKey(
        verbose_name="支出方",
        to=User,
        on_delete=models.DO_NOTHING,
        related_name='expend_side',
        help_text="花钱的一方",
        null=True,
        blank=True,
    )
    income_side = models.ForeignKey(
        verbose_name="收入方",
        to=User,
        on_delete=models.DO_NOTHING,
        related_name='income_side',
        help_text="收钱的一方",
        null=True,
        blank=True,
    )

    # 当发生经济活动中的某一方主体不是自然人，而是「商家」的时候，启用下面的字段
    business = models.ForeignKey(
        verbose_name="商家",
        to=Business,
        on_delete=models.DO_NOTHING,
        related_name='business',
        help_text="商家 或 平台",
        null=True,
        blank=True,
    )

    money_amount = models.DecimalField(
        verbose_name="金额",
        max_digits=10,
        decimal_places=3,
    )

    # 对当前这笔记录打上标签，便于后期按标签查找账单记录
    tags = models.ManyToManyField(
        verbose_name="标签",
        to=Tags,
        help_text="对当前这笔记录打上适合的标签，便于后期按标签查找账单记录",
        blank=True,
    )

    charge_comments = models.TextField(
        verbose_name="备注",
        max_length=200,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "记账"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "【" + str(self.created_at) + "】" + self.matter

from django.db import models
from django.contrib.auth.models import User
from account.models import *

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

    expend_side = models.ForeignKey(
        verbose_name="支出方",
        to=User,
        on_delete=models.DO_NOTHING,
        related_name='expend_side',
    )
    income_side = models.ForeignKey(
        verbose_name="收入方",
        to=User,
        on_delete=models.DO_NOTHING,
        related_name='income_side',
    )

    money_amount = models.DecimalField(
        verbose_name="金额",
        max_digits=10,
        decimal_places=3,
    )

    comments = models.TextField(
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

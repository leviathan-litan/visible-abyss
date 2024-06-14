from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):

    ACTIVE_CHOICE = [
        (0, '禁用'),
        (1, '启用'),
    ]
    ACCOUNT_TYPE_CHOICE = [
        (0, '商家'),
        (1, '个人'),
    ]

    user = models.ForeignKey(
        verbose_name="账户",
        to=User,
        on_delete=models.CASCADE,
    )

    active = models.IntegerField(
        verbose_name="是否启用",
        choices=ACTIVE_CHOICE,
        default=1,
    )

    account_type = models.IntegerField(
        verbose_name="账户类型",
        choices=ACCOUNT_TYPE_CHOICE,
        default=0,
    )

    comments = models.TextField(
        verbose_name="备注",
        max_length=200,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name="账户信息"
        verbose_name_plural=verbose_name

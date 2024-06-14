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

    user = models.OneToOneField(
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
        default=1,
    )

    comments = models.TextField(
        verbose_name="备注",
        max_length=200,
        null=True,
        blank=True,
    )

    wechat = models.CharField(
        verbose_name="微信号",
        max_length=200,
        null=True,
        blank=True,
    )
    alipay = models.CharField(
        verbose_name="支付宝",
        max_length=200,
        null=True,
        blank=True,
    )

    mobile = models.CharField(
        verbose_name="电话",
        max_length=30,
        null=True,
        blank=True,
    )
    email = models.CharField(
        verbose_name="电子邮箱",
        max_length=200,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name="账户信息"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.user.username

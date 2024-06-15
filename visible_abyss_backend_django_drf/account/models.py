from django.db import models
from django.contrib.auth.models import User

from tag.models import *

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

    # 标签
    tags = models.ManyToManyField(
        verbose_name="标签",
        to=Tags,
        help_text="打上合适的标签，便于后期按标签查找账单记录",
        blank=True,
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

    def __str__(self):
        return self.user.username

class Business(models.Model):

    business_name = models.CharField(
        verbose_name="商家名称",
        max_length=20,
    )

    # 标签
    tags = models.ManyToManyField(
        verbose_name="标签",
        to=Tags,
        help_text="打上合适的标签，便于后期按标签查找账单记录",
        blank=True,
    )

    business_comments = models.TextField(
        verbose_name="备注",
        max_length=200,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "商家"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.business_name

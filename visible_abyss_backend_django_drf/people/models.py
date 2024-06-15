from django.db import models

from tag.models import *
from work.models import *

# Create your models here.

class People(models.Model):

    peple_name = models.CharField(
        verbose_name="姓名",
        max_length=200,
    )

    # 工作
    work = models.ForeignKey(
        verbose_name="工作",
        to=Work,
        on_delete=models.CASCADE,
    )

    # 技能
    skill = models.ForeignKey(
        verbose_name="技能",
        to=Skill,
        on_delete=models.CASCADE,
    )
    
    people_comments = models.TextField(
        verbose_name="备注",
        max_length=200,
    )

    created_at = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        editable=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="更新时间",
        auto_now=True,
        editable=True,
    )

    class meta:
        verbose_name = "人"
        verbose_name_plural = verbose_name
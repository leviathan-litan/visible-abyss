from django.db import models

from tag.models import *
from work.models import *

# Create your models here.

class People(models.Model):

    peple_name = models.CharField(
        verbose_name="姓名",
        max_length=200,
    )

    # 工作：后期要通过从「工作经验」中查到的信息去跨表查询
    work = models.ForeignKey(
        verbose_name="工作",
        to=Work,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # 技能：后期要通过对「工作经验」中查到的信息去跨表查询
    skill = models.ForeignKey(
        verbose_name="技能",
        to=Skill,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    
    people_comments = models.TextField(
        verbose_name="备注",
        max_length=200,
        null=True,
        blank=True,
    )

    tags = models.ManyToManyField(
        verbose_name="标签",
        to=Tags,
        blank=True,
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

    class Meta:
        verbose_name = "人"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.peple_name

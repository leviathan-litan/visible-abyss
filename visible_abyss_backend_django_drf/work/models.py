from django.db import models

# Create your models here.

class Work(models.Model):

    work_name = models.CharField(
        verbose_name="工作",
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = "工作"
        verbose_name_plural = verbose_name

class Skill(models.Model):

    skill_name = models.CharField(
        verbose_name="技能",
        max_length=200,
        unique=True,
    )

    class Meta:
        verbose_name = "技能"
        verbose_name_plural = verbose_name

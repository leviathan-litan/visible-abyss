from django.db import models

# Create your models here.

class Tags(models.Model):

    tag_name = models.CharField(
        verbose_name="标签名",
        max_length=200,
        unique=True,
    )

    tag_comments = models.TextField(
        verbose_name="备注",
        max_length=200,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name

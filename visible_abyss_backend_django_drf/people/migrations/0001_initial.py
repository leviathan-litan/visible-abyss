# Generated by Django 5.0.6 on 2024-06-15 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("work", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="People",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("peple_name", models.CharField(max_length=200, verbose_name="姓名")),
                (
                    "people_comments",
                    models.TextField(max_length=200, verbose_name="备注"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
                (
                    "skill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="work.skill",
                        verbose_name="技能",
                    ),
                ),
                (
                    "work",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="work.work",
                        verbose_name="工作",
                    ),
                ),
            ],
        ),
    ]
# Generated by Django 5.0.6 on 2024-06-14 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Charge",
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
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="创建时间"),
                ),
                ("matter", models.CharField(max_length=200, verbose_name="事件名")),
                (
                    "money_amount",
                    models.DecimalField(
                        decimal_places=3, max_digits=10, verbose_name="金额"
                    ),
                ),
                ("comments", models.TextField(max_length=200, verbose_name="备注")),
                (
                    "expend_side",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="expend_side",
                        to="account.profile",
                        verbose_name="支出方",
                    ),
                ),
                (
                    "income_side",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="income_side",
                        to="account.profile",
                        verbose_name="收入方",
                    ),
                ),
            ],
            options={
                "verbose_name": "记账",
                "verbose_name_plural": "记账",
            },
        ),
    ]
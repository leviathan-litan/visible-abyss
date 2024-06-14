# Generated by Django 5.0.6 on 2024-06-14 17:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="charge",
            name="expend_side",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="expend_side",
                to=settings.AUTH_USER_MODEL,
                verbose_name="支出方",
            ),
        ),
        migrations.AlterField(
            model_name="charge",
            name="income_side",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="income_side",
                to=settings.AUTH_USER_MODEL,
                verbose_name="收入方",
            ),
        ),
    ]

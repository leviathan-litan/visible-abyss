# Generated by Django 5.0.6 on 2024-06-14 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="active",
            field=models.IntegerField(
                choices=[(0, "禁用"), (1, "启用")], default=1, verbose_name="是否启用"
            ),
        ),
    ]

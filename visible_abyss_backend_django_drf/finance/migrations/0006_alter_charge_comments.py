# Generated by Django 5.0.6 on 2024-06-14 17:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("finance", "0005_alter_charge_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="charge",
            name="comments",
            field=models.TextField(
                blank=True, max_length=200, null=True, verbose_name="备注"
            ),
        ),
    ]

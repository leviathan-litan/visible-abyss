# Generated by Django 5.0.6 on 2024-06-16 07:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("work", "0008_alter_department_department_description"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="work",
            options={"verbose_name": "工作 / 职业", "verbose_name_plural": "工作 / 职业"},
        ),
    ]

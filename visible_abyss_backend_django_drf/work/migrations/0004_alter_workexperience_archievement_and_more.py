# Generated by Django 5.0.6 on 2024-06-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("work", "0003_archievement_company_department_workexperience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workexperience",
            name="archievement",
            field=models.ManyToManyField(
                blank=True, to="work.archievement", verbose_name="成就"
            ),
        ),
        migrations.AlterField(
            model_name="workexperience",
            name="skills",
            field=models.ManyToManyField(
                blank=True, to="work.skill", verbose_name="技能"
            ),
        ),
    ]

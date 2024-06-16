# Generated by Django 5.0.6 on 2024-06-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("work", "0004_alter_workexperience_archievement_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="archievement",
            name="arch_description",
            field=models.TextField(
                blank=True, max_length=2000, null=True, verbose_name="描述"
            ),
        ),
        migrations.AddField(
            model_name="archievement",
            name="arch_name",
            field=models.CharField(
                default="暂无", max_length=200, unique=True, verbose_name="成就"
            ),
        ),
        migrations.AddField(
            model_name="workexperience",
            name="work_comments",
            field=models.TextField(
                blank=True, max_length=5000, null=True, verbose_name="备注"
            ),
        ),
    ]
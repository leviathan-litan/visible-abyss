# Generated by Django 5.0.6 on 2024-06-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0002_alter_people_options_alter_people_people_comments_and_more"),
        ("tag", "0003_alter_tags_tag_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="people",
            name="tags",
            field=models.ManyToManyField(blank=True, to="tag.tags", verbose_name="标签"),
        ),
    ]

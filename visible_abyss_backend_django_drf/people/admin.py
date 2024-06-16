from django.contrib import admin

from people.models import *

# Register your models here.

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = [
        'peple_name',
        'work',
        'skill',
        'people_comments',
        'show_tags',
        'created_at',
        'updated_at',
    ]

    # 在「展示界面」中「多对多」关系的呈现方式
    def show_tags(self, obj):

        # 遍历「tags」在命令行窗口中展示当前记录中所包含的标签数据
        for tag in obj.tags.all():
            print('--------------')
            print(tag.tag_name)

        # 返回数据
        return [tag.tag_name for tag in obj.tags.all()]

    show_tags.short_description = "标签"
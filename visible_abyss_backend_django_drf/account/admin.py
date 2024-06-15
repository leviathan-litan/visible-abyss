from django.contrib import admin

from account.models import *

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'active',
        'account_type',
        'show_tags',
        'comments',
    ]

    # 在「展示界面」中「多对多」关系的呈现方式
    def show_tags(self, obj):
        for tag in obj.tags.all():
            print('--------------')
            print(tag.tag_name)

        return [tag.tag_name for tag in obj.tags.all()]

    show_tags.short_description = "标签"


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = [
        'business_name',
        'show_tags',
        'business_comments',
    ]

    # 在「展示界面」中「多对多」关系的呈现方式
    def show_tags(self, obj):
        for tag in obj.tags.all():
            print('--------------')
            print(tag.tag_name)

        return [tag.tag_name for tag in obj.tags.all()]

    show_tags.short_description = "标签"

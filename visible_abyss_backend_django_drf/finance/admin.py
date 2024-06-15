from django.contrib import admin

from finance.models import *

# Register your models here.

@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = [
        'created_at',
        'matter',
        'business',
        'expend_side',
        'income_side',
        'money_amount',

        # 'tags',
        'show_tags',
        
        'charge_comments',
    ]

    date_hierarchy = "created_at"
    list_editable = [
        'business',
    ]
    list_display_links = [
        'matter',
    ]
    list_filter = [
        'expend_side',
        'income_side',
        'business',
        'created_at',
    ]

    # 在「展示界面」中「多对多」关系的呈现方式
    def show_tags(self, obj):
        for tag in obj.tags.all():
            print('--------------')
            print(tag.tag_name)

        return [tag.tag_name for tag in obj.tags.all()]

    show_tags.short_description = "标签"


from django.contrib import admin

from tag.models import *

# Register your models here.

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = [
        'tag_name',
        'tag_comments',
    ]
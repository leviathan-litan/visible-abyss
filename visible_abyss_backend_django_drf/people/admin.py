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
        'created_at',
        'updated_at',
    ]

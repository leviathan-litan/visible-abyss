from django.contrib import admin

from work.models import *

# Register your models here.

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = [
        'work_name',
    ]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [
        'skill_name',
    ]


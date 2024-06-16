from django.contrib import admin

from work.models import *

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        'company_name',
        'company_description',
    ]

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        'department_name',
        'department_description',
    ]

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

@admin.register(Archievement)
class ArchievementAdmin(admin.ModelAdmin):
    list_display = [
        'arch_name',
        'arch_description',
        'created_at',
        'updated_at',
    ]

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'company',
        'department',
        'work',
        'begin_at',
        'end_at',
        'work_comments',
    ]

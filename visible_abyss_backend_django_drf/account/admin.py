from django.contrib import admin

from account.models import *

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'active',
        'comments',
    ]
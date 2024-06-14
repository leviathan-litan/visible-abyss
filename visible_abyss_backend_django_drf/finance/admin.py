from django.contrib import admin

from finance.models import *

# Register your models here.

@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = [
        'created_at',
        'matter',
        'expend_side',
        'income_side',
        'money_amount',
        'comments',
    ]
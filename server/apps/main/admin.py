# -*- coding: utf-8 -*-

from django.contrib import admin  # noqa: F401
from .models import Hour
# Register your models here.


@admin.register(Hour)
class HourAdmin(admin.ModelAdmin):
    list_display = ('person', 'time', 'clock_type')
    list_filter = ('clock_type',)

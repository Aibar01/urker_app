from _decimal import ROUND_DOWN
from decimal import Decimal
from django.contrib import admin
from .models import Employee, Position
from rangefilter.filter import DateRangeFilter
from django.contrib.auth.models import Group



admin.site.unregister(Group)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['zero_id', 'name', 'surname', 'email', 'mobile_number', 'position', 'hire_date', 'is_active']
    list_display_links = ['zero_id', 'name', 'surname']
    search_fields = ['id', 'name', 'surname', 'email', 'position__position']
    list_filter = [
        ['hire_date', DateRangeFilter],
        'position__position',
        'is_active',
    ]
    readonly_fields = ['rating_count']



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position)

from django.contrib import admin

from .models import Shift
from .shift_manager import ShiftManager


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['user', 'project', 'start_date']
    search_fields = [
        'user',
    ]
    list_filter = [
        'start_date',
        'user',
        'project__name'
    ]
    readonly_fields = [
        'shift_sum',
        'overwork_hours',
        'overwork_sum',
        'late_lunch_sum',
        'current_lunch_sum',
        'non_sleep_hours',
        'non_sleep_sum',
        'day_off_hours',
        'day_off_sum',
        'total',
    ]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.end_date:
            shift_calculator = ShiftManager(obj)
            shift_calculator.update(obj.__dict__)

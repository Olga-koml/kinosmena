from django.contrib import admin

from .models import Shift


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
        'is_late_lunch',
        'late_lunch_sum',
        'is_current_lunch',
        'current_lunch_sum',
        'non_sleep_hours',
        'non_sleep_sum',
        'day_off_hours',
        'day_off_sum',
        'total',
    ]

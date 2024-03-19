from django.contrib import admin

from reports.models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_date']
    search_fields = [
        'user',
    ]
    list_filter = [
        'start_date',
        'user',
        'project__name'
    ]
    readonly_fields = [
        'shift_rate',
        'overwork_hours',
        'overwork_rate',
        'is_late_lunch',
        'late_lunch',
        'is_current_lunch',
        'current_lunch',
        'non_sleep_hours',
        'non_sleep_rate',
        'total',
    ]


from .models import TelegramUser


@admin.register(TelegramUser)
class UserAdmin(admin.ModelAdmin):

    list_display = ('id', 'tid')
    


from rest_framework import serializers

from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = [
            'project',
            'user',
            'start_date',
            'end_date',
            'shift_rate',
            'overwork_hours',
            'overwork_rate',
            'non_sleep_hours',
            'non_sleep_rate',
            'is_current_lunch',
            'is_late_lunch',
            'total',
        ]
        read_only_fields = [
            'late_lunch',
            'current_lunch',
            'shift_rate',
            'overwork_hours',
            'overwork_rate',
            'non_sleep_hours',
            'non_sleep_rate',
            'total'
        ]
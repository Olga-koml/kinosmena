from rest_framework import serializers

from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = [
            'id',
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation[
            'project'] = instance.project.name if instance.project else None
        return representation

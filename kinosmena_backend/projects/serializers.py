from rest_framework import serializers

from api.validators import validate_dates, validate_project_name
from projects.models import Project
from shifts.serializers import ShiftShortSerializer


class ProjectSerializer(serializers.ModelSerializer):
    shifts = ShiftShortSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'name',
            'description',
            'start_date',
            'end_date',
            'shift_duration',
            'rest_duration',
            'shift_rate',
            'overtime_rate',
            'non_sleep_rate',
            'current_lunch_rate',
            'late_lunch_rate',
            'per_diem',
            'day_off_rate',
            'is_archive',
            'created',
            'user',
            'shifts',
            )
        read_only_fields = ('user', 'shifts',)

    def validate(self, data):
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        # if start_date is not None and end_date is not None:
        validate_dates(start_date, end_date)
        tid = self.context['request'].query_params.get('tid')
        validate_project_name(name=data.get('name'),
                              tid=tid)
        return data

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.full_clean()
        instance.save()
        return instance

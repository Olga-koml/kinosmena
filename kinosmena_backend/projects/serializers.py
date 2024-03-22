from rest_framework import serializers

from projects.models import Project

from api.validators import validate_dates
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
        return data

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.full_clean()
        return instance

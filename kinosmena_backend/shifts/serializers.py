from rest_framework import serializers

from projects.models import Project
from shifts.config import load_config

from shifts.models import Shift

config = load_config()


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift
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
            'current_lunch',
            'is_late_lunch',
            'late_lunch',
            'is_per_diem',
            'per_diem',
            'is_day_off',
            'day_off',
            'services',
            'total',
        ]
        read_only_fields = [
            'late_lunch',
            'current_lunch',
            'shift_rate',
            'overwork_hours',
            'overwork_rate',
            'current_lunch',
            'late_lunch',
            'non_sleep_hours',
            'non_sleep_rate',
            'per_diem',
            'day_off',
            'total',
            'user'
        ]

    def validate(self, data):
        errors = {}
        is_current_lunch = data.get('is_current_lunch')
        is_late_lunch = data.get('is_late_lunch')
        services = data.get('services')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if is_current_lunch and is_late_lunch:
            errors.setdefault('is_current_lunch', []).append(config.lunch.text)
            errors.setdefault('is_late_lunch', []).append(config.lunch.text)

        if services not in config.services.values:
            errors.setdefault('services', []).append(config.services.text)

        if (start_date is not None and
                not (config.datefield.min_value <= start_date <= config.datefield.max_value)):
            errors.setdefault('start_date', []).append(config.datefield.text)

        if (end_date is not None and
                not (config.datefield.min_value <= end_date <= config.datefield.max_value)):
            errors.setdefault('end_date', []).append(config.datefield.text)

        if (start_date is not None
                and end_date is not None and not (start_date < end_date)):
            errors.setdefault('end_date', []).append(config.datefield.text_2)

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation[
            'project'] = instance.project.name if instance.project else None

        return representation

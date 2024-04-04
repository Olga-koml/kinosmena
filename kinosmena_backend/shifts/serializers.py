from rest_framework import serializers
from django.db import transaction

from projects.models import Project
from shifts.config import load_config
from datetime import timedelta

from shifts.models import Shift
from shifts.shift_manager import ShiftManager
from users.models import TelegramUser

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
            'shift_sum',
            'overwork_hours',
            'overwork_sum',
            'non_sleep_hours',
            'non_sleep_sum',
            'is_current_lunch',
            'current_lunch_sum',
            'is_late_lunch',
            'late_lunch_sum',
            'is_per_diem',
            'per_diem_sum',
            'is_day_off',
            'is_coefficient_shift',
            'day_off_sum',
            'day_off_hours',
            'services_sum',
            'total',
        ]
        read_only_fields = [
            'late_lunch_sum',
            'current_lunch_sum',
            'shift_sum',
            'overwork_hours',
            'overwork_sum',
            'non_sleep_hours',
            'non_sleep_sum',
            'per_diem_sum',
            'day_off_hours',
            'day_off_sum',
            'total',
            'user'
        ]

    def validate(self, data):
        errors = {}
        tid = self.context['request'].query_params.get('tid')
        user = TelegramUser.objects.get(tid=tid)
        is_current_lunch = data.get('is_current_lunch')
        is_late_lunch = data.get('is_late_lunch')
        services_sum = data.get('services_sum')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if is_current_lunch and is_late_lunch:
            errors.setdefault('is_current_lunch', []).append(config.lunch.text)
            errors.setdefault('is_late_lunch', []).append(config.lunch.text)

        if (services_sum not in config.services.values
                and services_sum is not None):
            errors.setdefault('services_sum', []).append(config.services.text)

        if (start_date is not None and
                not (
                        config.datefield.min_value <= start_date <= config.datefield.max_value)):
            errors.setdefault('start_date', []).append(config.datefield.text)

        if (end_date is not None and
                not (
                        config.datefield.min_value <= end_date <= config.datefield.max_value)):
            errors.setdefault('end_date', []).append(config.datefield.text)

        if (start_date is not None
                and end_date is not None and not (start_date < end_date)):
            errors.setdefault('end_date', []).append(config.datefield.text_2)

        if start_date:
            existing_shifts = user.shifts.filter(
                start_date__lte=start_date,
                end_date__gte=start_date,
                project=data.get('project')
            )
            if self.instance:
                existing_shifts = existing_shifts.exclude(
                    id=self.instance.id
                )
            if existing_shifts.exists():
                errors.setdefault('start_date', []).append(
                    config.datefield.text_3
                )

        if end_date:
            existing_shifts = user.shifts.filter(
                start_date__lte=end_date,
                end_date__gte=end_date,
                project=data.get('project'))
            if self.instance:
                existing_shifts = existing_shifts.exclude(
                    id=self.instance.id
                )
            if existing_shifts.exists():
                errors.setdefault('end_date', []).append(
                    config.datefield.text_3
                )

        if errors:
            raise serializers.ValidationError(errors)

        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation[
            'project'] = instance.project.name if instance.project else None

        return representation

    @transaction.atomic
    def create(self, validated_data):
        end_date = validated_data.get('end_date')
        if end_date is not None:
            instance = super().create(validated_data)
            shift_calculator = ShiftManager(instance)
            shift_calculator.update(validated_data)
            return instance

        return super().create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        end_date = validated_data.get('end_date')

        if end_date is not None:
            shift_calculator = ShiftManager(instance)
            shift_calculator.update(validated_data)

        validated_data['services_sum'] = instance.services_sum
        return super().update(instance, validated_data)


class ShiftShortSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField(read_only=True, )

    class Meta:
        model = Shift
        fields = (
            'id',
            'start_date',
            'end_date',
            'is_active',
        )

    def get_is_active(self, obj):
        if obj.end_date is None:
            return True
        else:
            return False

from rest_framework import serializers
from django.db import transaction

from projects.models import Project
from shifts.config import load_config
from datetime import timedelta

from shifts.models import Shift
import math
from shifts.shift_manager import ShiftManager

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
        is_current_lunch = data.get('is_current_lunch')
        is_late_lunch = data.get('is_late_lunch')
        services_sum = data.get('services_sum')
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if is_current_lunch and is_late_lunch:
            errors.setdefault('is_current_lunch', []).append(config.lunch.text)
            errors.setdefault('is_late_lunch', []).append(config.lunch.text)

        if services_sum not in config.services.values:
            errors.setdefault('services_sum', []).append(config.services.text)

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

    # def create(self, validated_data):
    #     project = validated_data.get('project')
    #     if project:
    #         validated_data['shift_rate'] = project.shift_rate
    #         validated_data['overwork_rate'] = project.overtime_rate
    #     return super().create(validated_data)



    # @transaction.atomic
    # def create(self, validated_data):
    #     end_date = validated_data.get('end_date')
    #     if end_date is not None:

    #         instance = super().create(validated_data)
    #         shift_calculator = ShiftManager(instance)
    #         shift_calculator.update(validated_data)
   
    #         return instance


    #     return super().create(validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        end_date = instance.end_date

        if end_date is not None:
            shift_calculator = ShiftManager(instance)

            shift_calculator.update(validated_data)

        instance.save()
        return super().update(instance, validated_data)


    # @transaction.atomic
    # def update(self, instance, validated_data):
    #     end_date = validated_data.get('end_date')
    #     manager = ShiftCalculate(instance)
    #     manager.update(validated_data)
        # if end_date and instance.end_date:
        #     project = validated_data.get('project', instance.project)
        #     if project:
        #         shift_sum = project.shift_rate
        #         validated_data['shift_rate'] = shift_sum
        #         start_date = instance.start_date
        #         shift_duration = timedelta(hours=project.shift_duration)
        #         print(shift_duration, 'SHIFT DURATION')

        #         overtime_hours = math.ceil(
        #             ((end_date - start_date - shift_duration).total_seconds() / 3600)
        #         ) if start_date + shift_duration < end_date else 0
        #         print(overtime_hours, 'OTVERTIME HOURS')
        #         overwork_sum = project.overtime_rate * overtime_hours
        #         print(overwork_sum, "СУММА ПЕРЕРАБОТКИ")
        #         validated_data['overwork_hours'] = overtime_hours
        #         validated_data['overwork_rate'] = overwork_sum
        #         current_lunch_sum = project.current_lunch_rate if instance.is_current_lunch else 0
        #         validated_data['current_lunch'] = current_lunch_sum
        #         late_lunch_sum = project.late_lunch_rate if instance.is_late_lunch else 0
        #         validated_data['late_lunch'] = late_lunch_sum
        #         per_diem = project.per_diem if instance.is_per_diem else 0
        #         validated_data['per_diem'] = per_diem
        #         day_off = project.day_off_rate if instance.is_day_off else 0
        #         validated_data['day_off'] = day_off

        #        # Предыдущую смена, относительно этой, так как возможно редактировать любую
        #         previous_shift = Shift.objects.filter(
        #             project=project,
        #             end_date__lt=start_date
        #         ).order_by('-end_date').first()

        #         # Если предыдущая смена существует
        #         non_sleep_hours = 0
        #         if previous_shift:
        #             # Считаем отчетную дату недосыпа последней смены.
        #             # Возомжно вынести в отдельное поле в БД
        #             prev_shift_end_date = previous_shift.end_date
        #             prev_shift_start_date = previous_shift.start_date
        #             print(prev_shift_start_date, 'PREV START DATE')
        #             prev_fact_shift_duration = math.ceil((
        #                 prev_shift_end_date - prev_shift_start_date
        #                 ).total_seconds() / 3600)
        #             print(prev_fact_shift_duration, "ФАКТИЧЕСКАЯ СМЕНА")
        #             prev_date_start_non_sleep = (
        #                 prev_shift_start_date + timedelta(hours=prev_fact_shift_duration) if
        #                 prev_fact_shift_duration > project.shift_duration else
        #                 prev_shift_start_date + shift_duration)

        #             print(prev_shift_end_date, 'PREVIOUS END DATE')
        #             print(prev_date_start_non_sleep, 'НАЧАЛО ОТСЧЕТА НЕДОСЫПА прошлой смены')
        #             rest_duration = timedelta(hours=project.rest_duration)
        #             print(rest_duration, 'REST DURATION')
        #             non_sleep_hours = math.ceil(
        #                 (prev_date_start_non_sleep + rest_duration - start_date).total_seconds() / 3600
        #             ) if prev_date_start_non_sleep + rest_duration > start_date else 0
        #             print(non_sleep_hours, "NON SLEEP")

        #         non_sleep_sum = non_sleep_hours * project.non_sleep_rate
        #         print(non_sleep_sum, 'NON SLEEP SUMM')
        #         validated_data['non_sleep_hours'] = non_sleep_hours
        #         validated_data['non_sleep_rate'] = non_sleep_sum
        #         validated_data['total'] = (
        #             shift_sum + overwork_sum + current_lunch_sum +
        #             late_lunch_sum + per_diem + day_off + non_sleep_sum
        #         )

        # return super().update(instance, validated_data)


class ShiftShortSerializer(serializers.ModelSerializer):
    is_active = serializers.SerializerMethodField(read_only=True,)

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

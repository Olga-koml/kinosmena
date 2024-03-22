from rest_framework import serializers

from shifts.models import Shift


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
            'total',
            'user'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation[
            'project'] = instance.project.name if instance.project else None
        return representation


class ShiftShortSerializer(serializers.ModelSerializer):
    is_closed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Shift
        fields = (
            'id',
            'start_date',
            'end_date',
            'is_closed',
            )

    def get_is_closed(self, obj):
        if obj.end_date is None:
            return False
        else:
            return True

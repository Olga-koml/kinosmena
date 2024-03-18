from rest_framework import serializers

from shifts.models import Shift


class ShiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shift
        fields = [
            'user',
            'project',
            'start_date',
            'end_date',
            'created',
            'is_current_lunch',
            'is_late_lunch',
            'is_day_off',
            'status',
        ]

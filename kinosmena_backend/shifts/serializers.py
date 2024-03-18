from rest_framework import serializers

from shifts.models import Shift


class ShiftSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(read_only=True)
    start_date = serializers.DateTimeField(read_only=True)
    end_date = serializers.DateTimeField(read_only=True)

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

from rest_framework import serializers

from projects.models import Project

from .validators import validate_dates


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

    def validate(self, data):
        start_date = data['start_date']
        end_date = data['end_date']
        # if start_date is not None and end_date is not None:
        validate_dates(start_date, end_date)
        return data

    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.full_clean()
        return instance

from datetime import datetime
from django.utils import timezone
from rest_framework import serializers

from users.models import TelegramUser


def validate_dates(start_date, end_date):
    """
    Проверка корректности дат.
    """

    MIN_ALLOWED_DATE = datetime(
        2000, 1, 1, tzinfo=timezone.get_current_timezone()
    )
    MAX_ALLOWED_DATE = datetime(
        2099, 1, 1, tzinfo=timezone.get_current_timezone()
    )

    errors = {}
    print(timezone.now())
    # if start_date is not None:
    if (start_date is not None and
            not (MIN_ALLOWED_DATE <= start_date <= MAX_ALLOWED_DATE)):
        errors.setdefault('start_date', []).append(
            "Некорректная дата"
        )
    if (end_date is not None and
            not (MIN_ALLOWED_DATE <= end_date <= MAX_ALLOWED_DATE)):
        errors.setdefault('end_date', []).append(
            "Некорректная дата"
        )
    if (start_date is not None
            and end_date is not None and not (start_date < end_date)):
        errors.setdefault('end_date', []).append(
            "Дата окончания раньше даты начала"
        )

    if errors:
        raise serializers.ValidationError(errors)

    return (start_date, end_date)


def validate_project_name(name: str, tid: int):
    user = TelegramUser.objects.get(tid=tid)
    if user.projects.filter(name=name).exists():
        raise serializers.ValidationError(
            {'name': 'Проект с таким названием уже существует.'})
    return name
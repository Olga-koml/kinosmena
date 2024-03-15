from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)

from django.conf import settings


class ShiftDuratinonValidator:
    """
    Валидация продолжительности смены.
    """

    shift_duration_min_value = MinValueValidator(
        settings.MIN_VAL_SHIFT_DURATION,
        message=settings.MESSAGE_VAL_SHIFT_DURATION_VALID

    )

    shift_duration_max_value = MaxValueValidator(
        settings.MAX_VAL_SHIFT_DURATION,
        message=settings.MESSAGE_VAL_SHIFT_DURATION_VALID

    )

    @classmethod
    def validate_shift_duration(cls, value):
        cls.shift_duration_min_value(value)
        cls.shift_duration_max_value(value)


def validate_rate(value):
    rate_max_value = MaxValueValidator(
        settings.MAX_VALUE_RATE,
        message=settings.MESSAGE_VALUE_RATE_VALID
    )

    rate_min_value = MinValueValidator(
        settings.MIN_VALUE_RATE,
        message=settings.MESSAGE_VALUE_RATE_VALID
    )

    rate_min_value(value)
    rate_max_value(value)

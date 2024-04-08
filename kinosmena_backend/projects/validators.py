from django.core.validators import (
    MaxLengthValidator,
    MaxValueValidator,
    MinValueValidator,
    RegexValidator
)

from django.conf import settings
from django.utils import timezone


class TextValidator:
    """
    Проверка введного текста.
    """

    text_regex = RegexValidator(
        regex=r'^[а-яА-ЯёЁa-zA-Z0-9_ .]+$',
        message=settings.MESSAGE_TEXT_REGEX_VALID
    )
    name_max_length = MaxLengthValidator(
        settings.MAX_LEN_NAME,
        message=settings.MESSAGE_MAX_LEN_NAME_VALID
    )

    description_max_length = MaxLengthValidator(
        settings.MAX_LEN_DESCRIPTION,
        message=settings.MESSAGE_MAX_LEN_DESCRIPTION_VALID
    )

    @classmethod
    def validate_name(cls, value):
        cls.text_regex(value)
        cls.name_max_length(value)

    @classmethod
    def validate_description(cls, value):
        cls.text_regex(value)
        cls.description_max_length(value)


class HoursValidator:
    """
    Валидация продолжительности смены/отдыха в часах.
    """

    duration_min_hours = MinValueValidator(
        settings.MIN_HOURS,
        message=settings.MESSAGE_MIN_HOURS_VALID

    )

    duration_max_hours = MaxValueValidator(
        settings.MAX_HOURS,
        message=settings.MESSAGE_MAX_HOURS_VALID

    )

    @classmethod
    def validate_shift_duration(cls, value):
        cls.duration_min_hours(value)
        cls.duration_max_hours(value)


class RateValidator:
    """
    Валидация стоимости смен, переработок
    """

    rate_max_value = MaxValueValidator(
        settings.MAX_VALUE_RATE,
        message=settings.MESSAGE_MAX_VALUE_RATE_VALID
    )

    rate_min_value = MinValueValidator(
        settings.MIN_VALUE_RATE,
        message=settings.MESSAGE_MIN_VALUE_RATE_VALID
    )

    shift_rate_max_value = MaxValueValidator(
        settings.MAX_VALUE_SHIFT_RATE,
        message=settings.MESSAGE_MAX_VALUE_SHIFT_RATE_VALID
    )

    @classmethod
    def validate_rate(cls, value):
        cls.rate_min_value(value)
        cls.rate_max_value(value)
    
    # в новых ТЗ убрали 9 значное число. Поэтому надо будет убрать, если снова не добавят
    @classmethod
    def validate_shift_rate(cls, value):
        cls.rate_min_value(value)
        cls.shift_rate_max_value(value)


class DateValidator:
    min_date = MinValueValidator(
        timezone.make_aware(timezone.datetime(2000, 1, 1)),
        'Некорректная дата'
    )
    max_date = MaxValueValidator(
        timezone.make_aware(timezone.datetime(2099, 1, 1)),
        'Некорректная дата'
    )

    @classmethod
    def validate_date(cls, value):
        cls.min_date(value)
        cls.max_date(value)

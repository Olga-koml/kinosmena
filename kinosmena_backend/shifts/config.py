from dataclasses import dataclass
from datetime import datetime
from django.utils import timezone


@dataclass
class ServiceField:
    text = 'Убедитесь, что это значение меньше либо равно 999999.'
    values = range(0, 1000000)


@dataclass
class DateField:
    text = 'Некорректная дата.'
    text_2 = 'Дата окончания не может быть раньше даты начала.'
    min_value = datetime(2000, 1, 1, tzinfo=timezone.get_current_timezone())
    max_value = datetime(2099, 1, 1, tzinfo=timezone.get_current_timezone())


@dataclass
class LunchField:
    text = 'Либо то, либо это :).'


@dataclass
class ShiftConfig:
    services: ServiceField
    lunch: LunchField
    datefield: DateField
    active_shift_error = 'Убедитесь, что все смены в этом проекте завершены'


def load_config() -> ShiftConfig:
    return ShiftConfig(
        services=ServiceField(),
        lunch=LunchField(),
        datefield=DateField()
    )

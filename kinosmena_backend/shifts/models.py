from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now

from projects.models import Project
from users.models import TelegramUser


class Shift(models.Model):
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        verbose_name='проект',
        related_name='shifts'
    )
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE,
        related_name='shifts',
        verbose_name='Пользователь'
    )
    start_date = models.DateTimeField(
        default=now,
        verbose_name='Начало смены',
    )
    end_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Конец смены',
    )
    is_current_lunch = models.BooleanField(
        default=False,
        verbose_name='текущий обед'
    )
    is_late_lunch = models.BooleanField(
        default=False,
        verbose_name='поздний обед'
    )
    is_per_diem = models.BooleanField(
        verbose_name='Суточные',
        default=False
    )
    is_day_off = models.BooleanField(
        verbose_name='смена в day-off',
        default=False
    )
    services_sum = models.IntegerField(
        verbose_name='Дополнительные услуги',
        default=0
    )

    shift_sum = models.IntegerField(
        verbose_name='цена за смену',
        default=0
    )
    overwork_hours = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        verbose_name='часы переработки'
    )
    overwork_sum = models.PositiveIntegerField(
        verbose_name='сумма переработок',
        default=0
    )
    non_sleep_hours = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        verbose_name='часы недосыпа'
    )
    non_sleep_sum = models.PositiveIntegerField(
        verbose_name='сумма недосыпов',
        default=0
    )
    current_lunch_sum = models.PositiveIntegerField(
        verbose_name='текущий обед',
        default=0
    )
    late_lunch_sum = models.PositiveIntegerField(
        verbose_name='поздний обед',
        default=0
    )
    day_off_sum = models.PositiveIntegerField(
        verbose_name='сумма в Day-off',
        default=0
    )
    day_off_hours = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        verbose_name='часы переработки в day-off'
    )
    per_diem_sum = models.IntegerField(
        verbose_name='Суточные',
        default=0
    )
    total = models.PositiveIntegerField(
        verbose_name='итого',
        default=0
    )

    def __str__(self):
        return f'{self.user} | {self.project} | {self.start_date}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'смена'
        verbose_name_plural = 'смены'

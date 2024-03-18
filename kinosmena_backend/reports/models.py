from django.db import models

from projects.models import Project
from users.models import TelegramUser


class Report(models.Model):
    project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        verbose_name='проект',
        related_name='reports'
    )
    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE,
        related_name='reports',
        verbose_name='Пользователь'
    )
    start_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Начало смены',
    )

    end_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Конец смены',
    )
    shift_rate = models.IntegerField(
        verbose_name='цена за смену'
    )
    overwork_hours = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        verbose_name='часы переработки'
    )
    overwork_rate = models.PositiveIntegerField(
        verbose_name='сумма переработок',
        default=0
    )
    non_sleep_hours = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        verbose_name='часы недосыпа'
    )
    non_sleep_rate = models.PositiveIntegerField(
        verbose_name='сумма недосыпов',
        default=0
    )
    is_current_lunch = models.BooleanField(
        default=False,
        verbose_name='текущий обед'
    )
    current_lunch = models.PositiveIntegerField(
        verbose_name='текущий обед',
        default=0
    )
    is_late_lunch = models.BooleanField(
        default=False,
        verbose_name='поздний обед'
    )
    late_lunch = models.PositiveIntegerField(
        verbose_name='поздний обед',
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
        verbose_name = 'отчет'
        verbose_name_plural = 'отчеты'
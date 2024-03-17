from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from .validators import ShiftDuratinonValidator, validate_rate

User = get_user_model()


class Project(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='projects'
        )

    name = models.CharField(
        max_length=settings.MAX_LEN_NAME,
        verbose_name='Название проекта'
    )

    description = models.CharField(
        max_length=settings.MAX_LEN_DESCRIPTION,
        blank=True,
        verbose_name='Описание проекта'
    )

    start_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата начала проекта',
    )

    end_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Дата окончания проекта',
    )

    shift_duration = models.IntegerField(
        default=settings.DEFAULT_SHIFT_DURATION,
        verbose_name='Продолжительность смены в часах',
        validators=[ShiftDuratinonValidator.validate_shift_duration],
    )

    shift_rate = models.IntegerField(
        verbose_name='Стоимость смены',
    )

    overtime_rate = models.IntegerField(
        verbose_name='Стоимость переработки в час',
        validators=[validate_rate]
    )

    non_sleep_rate = models.IntegerField(
        verbose_name='Стоимость недосыпа в час',
        validators=[validate_rate]
    )

    current_lunch_rate = models.IntegerField(
        verbose_name='Стоимость текущего обеда',
        validators=[validate_rate]
    )

    late_lunch_rate = models.IntegerField(
        verbose_name='Стоимость позднего обеда',
        validators=[validate_rate]
    )

    per_diem = models.IntegerField(
        verbose_name='Суточные',
        validators=[validate_rate]
    )

    day_off_rate = models.IntegerField(
        verbose_name='Стоимость Day-off',
        validators=[validate_rate]
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    #  назвала архивом!!! проверить
    is_archive = models.BooleanField(
        default=False,
        verbose_name='Архив проекта'
    )

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name

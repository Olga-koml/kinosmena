from django.db import models
from django.conf import settings
# from django.contrib.auth import get_user_model

from users.models import TelegramUser
from .validators import HoursValidator, RateValidator, TextValidator

# User = get_user_model()


class Project(models.Model):

    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE,
        related_name='projects'
        )

    name = models.CharField(
        max_length=settings.MAX_LEN_NAME,
        verbose_name='Название проекта',
        validators=[TextValidator.validate_name]
    )

    description = models.CharField(
        max_length=settings.MAX_LEN_DESCRIPTION,
        blank=True,
        verbose_name='Описание проекта',
        validators=[TextValidator.validate_description]
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
        default=settings.DEFAULT_HOURS_DURATION,
        verbose_name='Продолжительность смены в часах',
        validators=[HoursValidator.validate_shift_duration]
    )

    rest_duration = models.IntegerField(
        blank=True,
        null=True,
        # default=settings.DEFAULT_HOURS_DURATION,
        verbose_name='Шаг смены',
        validators=[HoursValidator.validate_shift_duration]
    )

    shift_rate = models.IntegerField(
        verbose_name='Стоимость смены',
        validators=[RateValidator.validate_shift_rate]
    )

    overtime_rate = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Стоимость переработки в час',
        validators=[RateValidator.validate_rate]
    )

    non_sleep_rate = models.IntegerField(
        verbose_name='Стоимость недосыпа в час',
        blank=True,
        null=True,
        validators=[RateValidator.validate_rate]
    )

    current_lunch_rate = models.IntegerField(
        verbose_name='Стоимость текущего обеда',
        blank=True,
        null=True,
        validators=[RateValidator.validate_rate]
    )

    late_lunch_rate = models.IntegerField(
        verbose_name='Стоимость позднего обеда',
        blank=True,
        null=True,
        validators=[RateValidator.validate_rate]
    )

    per_diem = models.IntegerField(
        verbose_name='Суточные',
        blank=True,
        null=True,
        validators=[RateValidator.validate_rate]
    )

    day_off_rate = models.IntegerField(
        verbose_name='Стоимость Day-off',
        blank=True,
        null=True,
        validators=[RateValidator.validate_rate]
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
        unique_together = ['name', 'user']

    def __str__(self):
        return self.name

    # def clean(self):
    #     if self.current_lunch_rate is None:
    #         self.current_lunch_rate = 8
    #     if self.overtime_rate is None:
    #         self.overtime_rate = 0
    #     if self.non_sleep_rate is None:
    #         self.non_sleep_rate = 0
    #     if self.late_lunch_rate is None:
    #         self.late_lunch_rate = 0
    #     if self.per_diem is None:
    #         self.per_diem = 0
    #     if self.day_off_rate is None:
    #         self.day_off_rate = 0

    #     super().clean()

    def clean(self):
        attributes_to_check = [
            'current_lunch_rate',
            'overtime_rate',
            'non_sleep_rate',
            'late_lunch_rate',
            'per_diem',
            'day_off_rate'
        ]
        for attr_name in attributes_to_check:
            attr_value = getattr(self, attr_name)
            if attr_value is None:
                setattr(self, attr_name, 0)
        if self.rest_duration is None:
            self.rest_duration = settings.DEFAULT_HOURS_DURATION
        super().clean()

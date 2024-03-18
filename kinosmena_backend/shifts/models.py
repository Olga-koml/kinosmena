from django.db import models
from django.contrib.auth import get_user_model

from projects.models import Project
from users.models import TelegramUser

User = get_user_model()


class Shift(models.Model):

    class Status(models.TextChoices):
        STARTED = 'ST', 'Started'
        FINISHED = 'F', 'Finished'
        DRAFT = 'DF', 'Draft'

    user = models.ForeignKey(
        TelegramUser, on_delete=models.CASCADE,
        related_name='shifts'
        )

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name='shifts'
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

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    is_current_lunch = models.BooleanField(
        default=False,
        verbose_name='текущий обед'
    )

    is_late_lunch = models.BooleanField(
        default=False,
        verbose_name='поздний обед'
    )

    is_day_off = models.BooleanField(
        default=False,
        verbose_name='day-off'
    )

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'

    def __str__(self):
        return self.project.name

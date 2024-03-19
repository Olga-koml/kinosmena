from django.db import models


class TelegramUser(models.Model):

    tid = models.PositiveBigIntegerField(
        primary_key=True,
        unique=True,
        verbose_name='Telegram ID',
    )

    def __str__(self):
        return f'{self.tid}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

from django.db import models


class TelegramUser(models.Model):

    tid = models.PositiveBigIntegerField(
        unique=True,
        verbose_name='Telegram ID',
    )

    def __str__(self):
        return f'{self.tid}'

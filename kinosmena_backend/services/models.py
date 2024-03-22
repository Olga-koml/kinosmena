from django.db import models

from shifts.models import Shift


class Service(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name='название услуги'
    )
    price = models.IntegerField(
        verbose_name='цена за услугу'
    )
    count = models.IntegerField(
        verbose_name='количество'
    )
    shift = models.ForeignKey(
        to=Shift,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

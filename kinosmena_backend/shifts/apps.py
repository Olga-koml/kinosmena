from django.apps import AppConfig


class ShiftsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shifts'

    # это для работы сигналов и сохранения БД на уровне модели по логике описанной в signals.py
    # def ready(self):
    #     import shifts.signals

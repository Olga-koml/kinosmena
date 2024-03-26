# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import Shift

# # позволяет создать сигнал который берет данные из модели проект в момент создания и редактирования смены
# @receiver(pre_save, sender=Shift)
# def update_shift_rates(sender, instance, **kwargs):
#     print("Signal triggered for Shift model")
#     if instance.project:
#         instance.shift_rate = instance.project.shift_rate
#         instance.overwork_rate = instance.project.overtime_rate or 0

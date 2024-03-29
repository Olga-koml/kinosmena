# Generated by Django 5.0.3 on 2024-03-28 14:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Начало смены')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Конец смены')),
                ('is_current_lunch', models.BooleanField(default=False, verbose_name='текущий обед')),
                ('is_late_lunch', models.BooleanField(default=False, verbose_name='поздний обед')),
                ('is_per_diem', models.BooleanField(default=False, verbose_name='Суточные')),
                ('is_day_off', models.BooleanField(default=False, verbose_name='смена в day-off')),
                ('services_sum', models.IntegerField(default=0, verbose_name='Дополнительные услуги')),
                ('shift_sum', models.IntegerField(default=0, verbose_name='цена за смену')),
                ('overwork_hours', models.PositiveSmallIntegerField(default=0, verbose_name='часы переработки')),
                ('overwork_sum', models.PositiveIntegerField(default=0, verbose_name='сумма переработок')),
                ('non_sleep_hours', models.PositiveSmallIntegerField(default=0, verbose_name='часы недосыпа')),
                ('non_sleep_sum', models.PositiveIntegerField(default=0, verbose_name='сумма недосыпов')),
                ('current_lunch_sum', models.PositiveIntegerField(default=0, verbose_name='текущий обед')),
                ('late_lunch_sum', models.PositiveIntegerField(default=0, verbose_name='поздний обед')),
                ('day_off_sum', models.PositiveIntegerField(default=0, verbose_name='сумма в Day-off')),
                ('day_off_hours', models.PositiveSmallIntegerField(default=0, verbose_name='часы переработки в day-off')),
                ('per_diem_sum', models.IntegerField(default=0, verbose_name='Суточные')),
                ('total', models.PositiveIntegerField(default=0, verbose_name='итого')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='projects.project', verbose_name='проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='users.telegramuser', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'смена',
                'verbose_name_plural': 'смены',
                'ordering': ['-id'],
            },
        ),
    ]

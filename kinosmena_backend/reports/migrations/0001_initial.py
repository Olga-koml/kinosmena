# Generated by Django 5.0.3 on 2024-03-19 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Начало смены')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Конец смены')),
                ('shift_rate', models.IntegerField(default=0, verbose_name='цена за смену')),
                ('overwork_hours', models.PositiveSmallIntegerField(default=0, verbose_name='часы переработки')),
                ('overwork_rate', models.PositiveIntegerField(default=0, verbose_name='сумма переработок')),
                ('non_sleep_hours', models.PositiveSmallIntegerField(default=0, verbose_name='часы недосыпа')),
                ('non_sleep_rate', models.PositiveIntegerField(default=0, verbose_name='сумма недосыпов')),
                ('is_current_lunch', models.BooleanField(default=False, verbose_name='текущий обед')),
                ('current_lunch', models.PositiveIntegerField(default=0, verbose_name='текущий обед')),
                ('is_late_lunch', models.BooleanField(default=False, verbose_name='поздний обед')),
                ('late_lunch', models.PositiveIntegerField(default=0, verbose_name='поздний обед')),
                ('day_off', models.PositiveIntegerField(default=0, verbose_name='Day-off')),
                ('is_per_diem', models.BooleanField(default=False, verbose_name='Суточные')),
                ('per_diem', models.IntegerField(default=0, verbose_name='Суточные')),
                ('total', models.PositiveIntegerField(default=0, verbose_name='итого')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='projects.project', verbose_name='проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='users.telegramuser', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'отчет',
                'verbose_name_plural': 'отчеты',
                'ordering': ['-id'],
            },
        ),
    ]

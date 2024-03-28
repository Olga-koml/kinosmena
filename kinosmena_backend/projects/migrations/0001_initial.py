# Generated by Django 5.0.3 on 2024-03-28 14:31

import django.db.models.deletion
import projects.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, validators=[projects.validators.TextValidator.validate_name], verbose_name='Название проекта')),
                ('description', models.CharField(blank=True, max_length=50, validators=[projects.validators.TextValidator.validate_description], verbose_name='Описание проекта')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата начала проекта')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания проекта')),
                ('shift_duration', models.IntegerField(default=8, validators=[projects.validators.HoursValidator.validate_shift_duration], verbose_name='Продолжительность смены в часах')),
                ('rest_duration', models.IntegerField(blank=True, null=True, validators=[projects.validators.HoursValidator.validate_shift_duration], verbose_name='Шаг смены')),
                ('shift_rate', models.IntegerField(validators=[projects.validators.RateValidator.validate_shift_rate], verbose_name='Стоимость смены')),
                ('overtime_rate', models.IntegerField(blank=True, null=True, validators=[projects.validators.RateValidator.validate_rate], verbose_name='Стоимость переработки в час')),
                ('non_sleep_rate', models.IntegerField(blank=True, null=True, validators=[projects.validators.RateValidator.validate_rate], verbose_name='Стоимость недосыпа в час')),
                ('current_lunch_rate', models.IntegerField(blank=True, null=True, validators=[projects.validators.RateValidator.validate_rate], verbose_name='Стоимость текущего обеда')),
                ('late_lunch_rate', models.IntegerField(blank=True, null=True, validators=[projects.validators.RateValidator.validate_rate], verbose_name='Стоимость позднего обеда')),
                ('per_diem', models.IntegerField(blank=True, null=True, validators=[projects.validators.RateValidator.validate_rate], verbose_name='Суточные')),
                ('day_off_rate', models.IntegerField(blank=True, null=True, validators=[projects.validators.RateValidator.validate_rate], verbose_name='Стоимость Day-off')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_archive', models.BooleanField(default=False, verbose_name='Архив проекта')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='users.telegramuser')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]

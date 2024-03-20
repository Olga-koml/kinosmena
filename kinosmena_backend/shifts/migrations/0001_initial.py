# Generated by Django 5.0.3 on 2024-03-20 18:18

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
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Начало смены')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='Конец смены')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_current_lunch', models.BooleanField(default=False, verbose_name='текущий обед')),
                ('is_late_lunch', models.BooleanField(default=False, verbose_name='поздний обед')),
                ('is_day_off', models.BooleanField(default=False, verbose_name='day-off')),
                ('status', models.CharField(choices=[('ST', 'Started'), ('F', 'Finished'), ('DF', 'Draft')], default='DF', max_length=2, verbose_name='Статус')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='projects.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='users.telegramuser')),
            ],
            options={
                'verbose_name': 'смена',
                'verbose_name_plural': 'смены',
            },
        ),
    ]

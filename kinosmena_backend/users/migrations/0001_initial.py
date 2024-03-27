# Generated by Django 5.0.3 on 2024-03-27 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('tid', models.PositiveBigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Telegram ID')),
            ],
            options={
                'verbose_name': 'пользователь',
                'verbose_name_plural': 'пользователи',
            },
        ),
    ]

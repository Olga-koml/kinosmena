from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# class TelegramUser(models.Model):

#     tid = models.PositiveBigIntegerField(
#         unique=True,
#         verbose_name='Telegram ID',
#     )

#     def __str__(self):
#         return f'{self.tid}'

#     class Meta:
#         verbose_name = 'пользователь'
#         verbose_name_plural = 'пользователи'


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
 
    def _create_user(self, tid, password=None, **extra_fields):
        if not tid:
            raise ValueError('Users require a telegram_id field')
        user = self.model(tid=tid, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, tid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(tid, password, **extra_fields)

    def create_superuser(self, tid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(tid, password, **extra_fields)


class TelegramUser(AbstractUser):

    username = None
    tid = models.PositiveBigIntegerField(
        unique=True,
        verbose_name='Telegram ID',
    )
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'tid'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('date_joined',)

    def __str__(self):
        return f'{self.tid}'
    
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Кастомная модель пользователя с авторизацией по email."""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    city = models.CharField('Город', max_length=100, blank=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/', blank=True, null=True)

    username = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email or self.username or str(self.id)

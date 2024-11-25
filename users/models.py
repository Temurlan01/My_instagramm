from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []

    nickname = models.CharField(unique=True, db_index=True, max_length=50, default=None)

    avatar = models.ImageField(upload_to="avatars/")
    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'


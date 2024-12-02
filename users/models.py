from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = []

    nickname = models.CharField(unique=True, db_index=True, max_length=50, default=None)

    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'


class CustomUserFollower(models.Model):
    following = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='на кого подписался', related_name='my_followers')
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='кто подписан', related_name='my_following')
    created_at = models.DateTimeField(auto_now_add=True, null=True)


from django.db import models

from users.models import CustomUser


class Publication(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='my_publications', null=True)
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



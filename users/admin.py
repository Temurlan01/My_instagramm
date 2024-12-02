from django.contrib import admin

from users.models import CustomUser, CustomUserFollower


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['nickname',]

@admin.register(CustomUserFollower)
class CustomUserFollowerAdmin(admin.ModelAdmin):
    list_display = ['following','follower',]

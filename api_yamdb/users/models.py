from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    ROLE_CHOICES = [
        (USER, 'User'),
        (MODERATOR, 'Moderator'),
        (ADMIN, 'Admin'),
    ]
    role = models.CharField(
        max_length=10,
        verbose_name='Роль',
        help_text='Роль пользователя',
        choices=ROLE_CHOICES,
        default=USER,
    )

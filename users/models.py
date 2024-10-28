from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    # Add additional fields if needed
    phone_number = models.CharField(max_length=15, blank=True)

    # Specify unique related names
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Changed related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Changed related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

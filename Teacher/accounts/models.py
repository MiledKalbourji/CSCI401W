# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    id = models.AutoField(primary_key=True)
    # Since AbstractUser already includes fields like username, first_name, last_name, and email,
    # you may not need to redefine them unless you have specific requirements.
    # If you do redefine them, ensure they align with your application's needs.

    # You can add additional fields here if needed.
    # Example:
    # additional_field = models.CharField(max_length=100)
    
    # If you don't need to customize related_name, you can omit it.
    # If you do need it, make sure it's unique and doesn't conflict with other models.
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        verbose_name='user permissions',
    )

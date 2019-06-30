"""User models."""

#Django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#Utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """User model"""

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con este e-mail'
        }
    )

    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Indique un numero de telefono que cumpla con el formato +9999999999"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Saber si un usuario es cliente'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text=(
            'Saber si un usuario esta verificado'
        )
    )

    def __str__(self):
        """Return username"""
        return self.username

    def get_short_name(self):
        """Return username"""
        return self.username

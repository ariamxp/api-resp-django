"""Circle model"""

#Django
from django.db import models

#Utilities
from cride.utils.models import CRideModel


class Circle(CRideModel):
    """Circle models"""

    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=140)

    about = models.CharField('cirlce description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures', blank=True)

    #Stats
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text=(
            'Verificar usuarios de la comunidad'
        )
    )

    is_public = models.BooleanField(
        default=True,
        help_text=(
            'Saber si un circulo es publico o privado'
        )
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text=(
            'Saber si el circle tiene limite de miembros'
        )
    )

    members_limit = models.PositiveIntegerField(
        default=0,
        help_text=(
            'Numero limite de miembros de un circle'
        )
    )

    def __str__(self):
        """Return circle"""
        return self.name


    class Meta(CRideModel.Meta):
        """Meta class"""

        ordering = ['-rides_taken', '-rides_offered']

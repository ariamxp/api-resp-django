"""Django models utilities."""

#Django
from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model
    Esta es una clase abstracta que funcionará para todos
    los modelos del proyecto. Los atributos serán:
        + created (DateTime): fecha de creación
        + modified (DateTime): fecha de modificación
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Guarda la fecha de cuando se creó el registro'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Guarda la fecha de cuando se modificó el registro'
    )

    class Meta:
        """Meta options"""

        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']

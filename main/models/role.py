from django.db import models
from ..enums import UserRole

class Role(models.Model):
    key = models.CharField(choices=UserRole.choices, editable=False)
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=254, blank=False)

    def __str__(self):
        return f"{self.key}"
    
from django.db import models
from ..enums import UserRole

class Role(models.Model):
    key = models.IntegerField(choices = UserRole.choices())
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=254, blank=False)
    
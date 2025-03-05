from django.db import models
from .utils import UserRole

class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=100, blank=False)
    role = models.IntegerField(choices = UserRole.choices())
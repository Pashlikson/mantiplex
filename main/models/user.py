from django.db import models
from ..enums import UserRole
from .role import Role

class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    birth_date = models.DateField(blank=False, null=True)
    
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
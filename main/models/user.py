from django.db import models
from ..enums import UserRole
from .role import Role

class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    birth_date = models.DateField(blank=False, null=True)
    school = models.CharField(blank=False, null=True)
    
    role = models.ForeignKey(Role, on_delete=models.PROTECT) #//TODO: Delete role field?

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
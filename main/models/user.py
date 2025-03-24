from django.db import models
from django.contrib.auth.models import User as AuthUser
from .role import Role

class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    birth_date = models.DateField(blank=False, null=True)
    auth_user = models.ForeignKey(AuthUser, blank=False, on_delete=models.CASCADE)
    
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
from django.db import models
from .user import User

class Parent(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    job = models.CharField(max_length=20)
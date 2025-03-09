from django.db import models
from .user import User

class Student(models.Model):
    user = models.ForeignKey(User, blank=False)
    job = models.CharField(max_length=20)
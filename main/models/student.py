from django.db import models
from .user import User
from .school_class import School_class

class Student(models.Model):
    user = models.ForeignKey(User, blank=False)
    first_guardian = models.ForeignKey(User, blank=False)
    second_guardian = models.ForeignKey(User)
    school_class = models.ForeignKey(School_class, blank=False)
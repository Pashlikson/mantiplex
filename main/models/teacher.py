from django.db import models
from .user import User
from ..enums import TeacherSubject

class Teacher(models.Model):
    user = models.ForeignKey(User, blank=False)
    subject = models.CharField(TeacherSubject)
    eployment_year = models.IntegerField(max_length=4, blank=False)
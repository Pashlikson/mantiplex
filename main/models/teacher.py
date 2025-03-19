from django.db import models
from .user import User
from ..enums import TeacherSubject

class Teacher(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    subject = models.CharField(choices=TeacherSubject.choices)
    eployment_year = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
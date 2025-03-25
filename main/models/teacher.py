from django.db import models
from .user import User
from ..enums import TeacherSubject

class Teacher(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE, null=True)
    subject = models.CharField(choices=TeacherSubject.choices)
    employment_year = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
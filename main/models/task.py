from django.db import models
from django.utils.timezone import now
from main.enums import TaskStatus
from .user import User

class Task(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(max_length=56, blank=False)
    begin_time = models.DateField(blank=False, default=now)
    end_time = models.DateField(blank=False)
    context = models.CharField(max_length=325)
    status = models.CharField(choices=TaskStatus.choices)

    def __str__(self):
        return f"{self.name}"
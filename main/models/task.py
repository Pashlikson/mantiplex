from django.db import models
from django.utils.timezone import now
from main.enums import TaskStatus

class Task(models.Model):
    name = models.CharField(max_length=56, blank=False)
    begin_time = models.DateField(blank=False, default=now)
    end_time = models.DateField(blank=False)
    context = models.CharField(max_length=325)
    status = models.CharField(TaskStatus)
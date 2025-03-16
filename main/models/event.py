from django.db import models
from django.utils.timezone import now
from main.enums import EventStatus

class Event(models.Model):
    name = models.CharField(max_length=56, blank=False)
    begin_time = models.DateField(blank=False, default=now)
    end_time = models.DateField(blank=False)
    context = models.CharField(max_length=325)
    event_position = models.CharField()
    event_status = models.CharField(EventStatus)
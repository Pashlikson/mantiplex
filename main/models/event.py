from django.db import models
from django.utils.timezone import now
from main.enums import EventStatus
from .user import User

class Event(models.Model):
    customer = models.ForeignKey(User, on_delete=models.PROTECT, null=True)#//TODO: set blank = False
    name = models.CharField(max_length=56, blank=False)
    begin_time = models.DateField(blank=False, default=now)
    end_time = models.DateField(blank=False)
    context = models.CharField(max_length=325)
    event_adress = models.CharField(null=True, blank=False)
    event_status = models.CharField(choices=EventStatus.choices, editable=False)

    def __str__(self):
        return f"{self.name}"
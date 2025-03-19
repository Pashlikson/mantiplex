from django.db import models
from .user import User
from .parent import Parent
from .school_class import School_class

class Student(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    school_class = models.ForeignKey(School_class, blank=False, on_delete=models.PROTECT)
    first_guardian = models.ForeignKey(Parent, blank=False, on_delete=models.CASCADE, related_name='first_guardian')
    second_guardian = models.ForeignKey(Parent, on_delete=models.PROTECT, related_name='second_guardian')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
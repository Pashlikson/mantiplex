from django.db import models
from .teacher import Teacher
from .school_class import School_class
from ..enums import TeacherRole, TeacherSubject

class School_class_teacher(models.Model):
    teacher = models.ForeignKey(Teacher, blank=False, on_delete=models.PROTECT)
    school_class = models.ForeignKey(School_class, blank=False, on_delete=models.PROTECT)
    
    teacher_role = models.CharField(choices=TeacherRole.choices)
    subject = models.CharField(choices=TeacherSubject.choices)

    def __str__(self):
        return f"{self.teacher} {self.school_class}"
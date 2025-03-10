from django.db import models
from .teacher import Teacher
from .school_class import School_class
from ..enums import TeacherRole, TeacherSubject

class School_class_teacher(models.Model):
    teacher = models.ForeignKey(Teacher, blank=False, on_delete=models.CASCADE)
    school_class = models.ForeignKey(School_class, blank=False, on_delete=models.CASCADE)
    
    teacher_role = models.CharField(TeacherRole)
    subject = models.CharField(TeacherSubject)
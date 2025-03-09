from django.db import models
from .teacher import Teacher
from .school_class import School_class
from ..enums import TeacherRole, TeacherSubject

class School_class_teacher(models.Model):
    teacher = models.ForeignKey(Teacher, blank=False)
    school_class = models.ForeignKey(School_class, blank=False)
    
    teacher_role = models.CharField(TeacherRole)
    subject = models.CharField(TeacherSubject)
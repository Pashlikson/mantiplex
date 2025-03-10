from django.contrib import admin
from .models.user import User
from .models.school_class import School_class
from .models.school_class_teacher import School_class_teacher
from .models.parent import Parent
from .models.student import Student
from .models.teacher import Teacher
from .models.role import Role

# Register your models here.
admin.site.register(User)
admin.site.register(School_class)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(Role)
admin.site.register(School_class_teacher)
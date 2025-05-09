from django.contrib import admin
from .models.user import User
from .models.school_class import School_class
from .models.school_class_teacher import School_class_teacher
from .models.parent import Parent
from .models.student import Student
from .models.teacher import Teacher
from .models.role import Role
from .models.event import Event
from .models.task import Task
from django.contrib.auth.models import Group
    
class RoleAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False
    
class GroupAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request):
        return False
    
# Register your models here.
admin.site.register(User)
admin.site.register(School_class)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Teacher)
admin.site.register(Role, RoleAdmin)
admin.site.register(School_class_teacher)
admin.site.register(Event)
admin.site.register(Task)
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
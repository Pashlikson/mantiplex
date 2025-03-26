from django import forms
from main.models.role import Role
from main.models.student import Student, School_class
from main.models.parent import Parent
from main.models.teacher import Teacher
from main.enums import TeacherSubject

class ProfileForm(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=100)
    last_name = forms.CharField(label='Your last name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)
    birth_date = forms.DateField(label='Your birth day')
    role = forms.ModelChoiceField(queryset=Role.objects.all())

class StudentForm(forms.Form):
    school_class = forms.ModelChoiceField(queryset=School_class.objects.all())
    first_guardian = forms.ModelChoiceField(queryset=Parent.objects.all())
    second_guardian = forms.ModelChoiceField(queryset=Parent.objects.all())

class ParentForm(forms.Form):
    job = forms.CharField(label='your job', max_length=20)

class TeacherForm(forms.Form):
    subject = forms.ChoiceField(choices=TeacherSubject.choices())
    employment_year = forms.IntegerField(label='employment year')
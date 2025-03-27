from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from main.models.user import User
from main.models.parent import Parent
from main.models.teacher import Teacher
from main.models.student import Student
from .validators import profile_validation, redirect_profile_by_role,\
                        student_validation, parent_check, teacher_validation
from .decorators import unauthanticated_user
from .utils import convert_hex_into_cyrilic
from .forms import ProfileForm, StudentForm, ParentForm, TeacherForm


# register views:
@unauthanticated_user
def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_form = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'profile.html', {'form': form, 'errors': form.errors})
    else:
        form = UserCreationForm()
    return render(request, 'register_page.html', {
        'form': form
        })

@unauthanticated_user
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid() and profile_validation(form):
            main_user = User(first_name=form.cleaned_data['first_name'], 
                            last_name=form.cleaned_data['last_name'], 
                            email=form.cleaned_data['email'], 
                            role=form.cleaned_data['role'], 
                            birth_date=form.cleaned_data['birth_date'], 
                            auth_user_id=request.user
                            )
            main_user.save()
            return redirect(redirect_profile_by_role(form))
        else:
            message = 'Form(s) were filled incorrectly!'
            return render(request, 'profile.html', {'form': form, 'message': message, 'errors': form.errors})
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})

@unauthanticated_user
def student_profile(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        main_user = User.objects.get(auth_user_id=request.user.id)
        if form.is_valid() and student_validation(form, main_user):
            student = Student(user=main_user,
                              school_class=form.cleaned_data['school_class'],
                              first_guardian=form.cleaned_data['first_guardian'],
                              second_guardian=form.cleaned_data['second_guardian'])      
            student.save()
            my_group = Group.objects.get(name='Student')
            my_group.user_set.add(request.user.id)
            return redirect('main')
        else:
            print(student_validation(form, main_user))
            message = 'Form(s) were filled incorrectly!'
            return render(request, 'student_profile.html', {'form': form, 'message': message, 'errors': form.errors})
    else:
        form = StudentForm()
    return render(request, 'student_profile.html', {'form': form})

@unauthanticated_user
def parent_profile(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)
        if form.is_valid():
            main_user = User.objects.get(auth_user_id=request.user.id)
            parent = Parent(user=main_user,
                             job=form.cleaned_data['job'])     
            parent.save()
            my_group = Group.objects.get(name='Parent')
            my_group.user_set.add(request.user.id)
            if not parent_check(form):
                return redirect('teacher')
            return redirect('main')
        else:
            message = 'Form(s) were filled incorrectly!'
            return render(request, 'parent_profile.html', {'form': form, 'message': message, 'errors': form.errors})
    else:
        form = ParentForm()
    return render(request, 'parent_profile.html', {'form': form})

@unauthanticated_user
def teacher_profile(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        main_user = User.objects.get(auth_user_id=request.user.id)
        if form.is_valid() and teacher_validation(form, main_user):
            teacher = Teacher(user=main_user,
                              subject=form.cleaned_data['subject'],      
                              employment_year=form.cleaned_data['employment_year'])
            teacher.save()
            my_group = Group.objects.get(name='Teacher')
            my_group.user_set.add(request.user.id)
            return redirect('main')
        else:
            message = 'Form(s) were filled incorrectly!'
            return render(request, 'teacher_profile.html', {'form': form, 'message': message, 'errors': form.errors})
    else:
        form = TeacherForm()
    return render(request, 'teacher_profile.html', {'form': form})

# login view
def login_page(request):
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('calendar')
        else:
            return redirect('login')
    else:
        return render(request, 'login_page.html')

# main view
def main_page(request):
    convert = convert_hex_into_cyrilic('d093')
    return render(request, 'main.html', {
        'letter': convert,
    })

# calendar views
@login_required
def calendar_page(request):
    return render(request, 'calendar_page.html')

@login_required
def profile_page(request):
    my_profile = User.objects.get(auth_user_id=request.user.id)
    return render(request, 'own_profile.html', {
        'my_user': my_profile,
    })

@login_required
def users(request):
    return render(request, 'users.html')

@login_required
def user_profile(request):
    return render(request, 'user_profile.html')

@login_required
def event(request):
    return render(request, 'events.html')

@login_required
def event_detail(request):
    return render(request, 'event_detail.html')


# Just password
"""
c6{00}3=2=4&(#y^$UE$)

75by348b559nini54b[63b6y]

yrecycwtn85v76;4b8

8n4n3w95um;uy4bme6[i054m0]

6974yu23n6u5n0[6n953]
"""
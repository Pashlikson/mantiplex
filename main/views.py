"""File contains views for the main app of the project. 
It includes views for user registration, profile management, login,"""
# pylint: disable=E1101

from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse

from main.models.user import User
from main.models.parent import Parent
from main.models.teacher import Teacher
from main.models.student import Student
from main.models.event import Event
from main.models.task import Task
from .validators import profile_validation, redirect_profile_by_role,\
                        student_validation, parent_check, teacher_validation, check_date
from .decorators import unauthanticated_user
from .utils import HexLetterConventor, ConvertDatetime, filter_by_role
from .forms import ProfileForm, StudentForm, ParentForm, TeacherForm, EventForm, TaskForm

# register views:
@unauthanticated_user
def register_page(request):
    """ Register page view """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, form.errors if form.errors else 'Form was filled incorrectly!')
            return render(request, 'profile.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'register_page.html', {
        'form': form
        })

@unauthanticated_user
def profile(request):
    """ Profile view """
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
            messages.error(request, form.errors if form.errors else 'Form was filled incorrectly!')
            return render(request, 'profile.html', {'form': form})
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})

@unauthanticated_user
def student_profile(request):
    """ Student profile view """
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
            messages.success(request, 'User was created successfully!')
            return redirect('main')
        else:
            print(student_validation(form, main_user))
            messages.error(request, form.errors if form.errors else 'Form was filled incorrectly!')
            return render(request, 'student_profile.html', {'form': form})
    else:
        form = StudentForm()
    return render(request, 'student_profile.html', {'form': form})

@unauthanticated_user
def parent_profile(request):
    """ Parent profile view """
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
            messages.success(request, 'User was created successfully!')
            return redirect('main')
        else:
            messages.error(request, form.errors if form.errors else 'Form was filled incorrectly!')
            return render(request, 'parent_profile.html', {'form': form, })
    else:
        form = ParentForm()
    return render(request, 'parent_profile.html', {'form': form})

@unauthanticated_user
def teacher_profile(request):
    """ Teacher profile view """
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
            messages.success(request, 'User was created successfully!')
            return redirect('main')
        else:
            messages.error(request, form.errors if form.errors else 'Form was filled incorrectly!')
            return render(request, 'teacher_profile.html', {'form': form})
    else:
        form = TeacherForm()
    return render(request, 'teacher_profile.html', {'form': form})

# login view
def login_page(request):
    """ Login page view (User authentication) """
    if request.method == 'POST':
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            messages.success(request, 'Event was created successfully!')
            return redirect('calendar')
        else:
            messages.error(request, 'Login was failed!')
            return redirect('login')
    else:
        return render(request, 'login_page.html')

# main view
def main_page(request):
    """ Main page view """
    user = bool(User.objects.filter(auth_user_id=request.user.id).exists())
    convert = HexLetterConventor.convert_hex_into_cyrilic(hex_value='d093')
    return render(request, 'main.html', {
        'letter': convert,
        'user': user,
    })

# calendar views
@login_required
def calendar_page(request):
    """ Calendar page view """
    weeks = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']

    current_month = datetime.now().month
    current_year = datetime.now().year
    current_day = datetime.now().day

    selected_year = int(request.GET.get('year', current_year))
    selected_month = int(request.GET.get('month', current_month))
    selected_day = int(request.GET.get('day', current_day))

    selected_month_title = ConvertDatetime.convert_months(selected_month)
    selected_days = ConvertDatetime.convert_current_day(selected_year, selected_month)
    is_selected_month_current = selected_month == current_month and selected_year == current_year

    events = Event.objects.filter(begin_time__year=selected_year, begin_time__month=selected_month)
    tasks = Task.objects.filter(begin_time__year=selected_year, begin_time__month=selected_month)

    role = User.objects.get(auth_user_id=request.user.id).role

    form = EventForm(request.POST)
    return render(request, 'calendar_page_html/calendar_page.html', {
        'current_year': current_year, 
        'current_month': ConvertDatetime.convert_months(current_month), 
        'current_day': current_day,
        'weeks': weeks, 
        'selected_year': selected_year,
        'selected_month': selected_month_title,
        'selected_days': selected_days,
        'is_selected_month_current': is_selected_month_current,
        'form': form,
        'role': str(role),
        'massage': {"type": "success", "message": "Event was created successfully!"},
        'selected_year_month': datetime(year=selected_year, month=selected_month, day=selected_day).strftime("%Y-%m"),
        'events': events,
        'tasks': tasks,
        })

# Your profile views
@login_required
def profile_page(request):
    """ Your profile page view """
    my_profile = filter_by_role(request.user.id)
    return render(request, 'own_profile.html', {
        'my_user': my_profile['user'],
        'role': str(my_profile['user'].role),
        'role_user': my_profile['role_user']
    })

# Users views
@login_required
def users(request):
    """ List of all users """
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})

@login_required
def user_profile(request, id):
    """ User profile view """
    user_profile = User.objects.get(id=id)
    return render(request, 'user_profile.html', {'user': user_profile})

# Events and tasks views
@login_required
def event(request):
    """Create, update, delete and get events """
    if request.method == 'POST':
        #logic to create new event
        form = EventForm(request.POST)
        if form.is_valid() and check_date(form):
            if form.cleaned_data['url_adress'] is None or form.cleaned_data['adress'] is None:
                messages.error(request, 'Event adress and link must be filled!')
                redirect('calendar')
            else:
                new_event = Event(
                creator=User.objects.get(auth_user_id=request.user.id),
                name=form.cleaned_data['name'],
                begin_time=form.cleaned_data['start_date'],
                end_time=form.cleaned_data['end_date'],
                context=form.cleaned_data['context'],
                event_adress=form.cleaned_data['address'],
                event_url_adress=form.cleaned_data['url_address'],
                event_status=form.cleaned_data['status'],
                )
                new_event.save()
                messages.success(request, 'Event was created successfully!')
                return redirect('calendar')
        messages.error(request, form.errors if form.errors else 'Form was filled incorrectly!')
        return redirect('calendar')
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    elif request.method == 'GET':
        if request.GET.get('id'):
            pass
        else:
            pass
    my_profile = User.objects.get(auth_user_id=request.user.id).role
    events = Event.objects.all()
    tasks = Task.objects.all()
    return render(request, 'events.html', {'events': events, 'tasks': tasks, 'role': str(my_profile)})

@login_required
def task(request):
    """Create, update, delete and get tasks """
    if request.method == 'POST':
        #logic to create new event
        form = TaskForm(request.POST)
        if form.is_valid() and check_date(form):
            new_task = Task(
            creator=User.objects.get(auth_user_id=request.user.id),
            name=form.cleaned_data['name'],
            begin_time=form.cleaned_data['start_date'],
            end_time=form.cleaned_data['end_date'],
            context=form.cleaned_data['context'],
            status='0',
            )
            new_task.save()
            messages.success(request, 'Task was created successfully!')
            return redirect('calendar')
        messages.error(request, form.errors if form.errors else 'Form was filled incorrectly!')
        return redirect('calendar')
    if request.method == 'PUT':
        #logic to update event by id
        pass
    if request.method == 'DELETE':
        pass
    if request.method == 'GET':
        if request.GET.get('id'):
            pass
        else:
            pass
    return None

@login_required
def event_detail(request, id):
    """ Event detail view """
    my_event = Event.objects.get(id=id)
    if my_event.event_status == '0':
        event_status = 'Personal event'
    elif my_event.event_status == '1':
        event_status = 'School event'
    else:
        event_status = 'Parent meeting'
    return render(request, 'event_detail.html', {'my_event': my_event, 'event_status': event_status})

def event_list(request):
    """ Event list view """
    if request.method == 'GET':
        selected_date = request.GET.get('selected_date')
        if selected_date:
            date_format = '%Y-%m-%d'

            date_obj = datetime.strptime(selected_date, date_format)
            events = list(Event.objects.filter(begin_time__lte=date_obj, end_time__gte=date_obj).values())
            tasks = list(Task.objects.filter(begin_time__lte=date_obj, end_time__gte=date_obj).values())
            return JsonResponse({"events": events, "tasks": tasks})
        return JsonResponse({"events": [], "tasks": []})

@login_required
def task_detail(request, id):
    """ Task detail view """
    my_task = Task.objects.get(id=id)
    if my_task.status == '0':
        task_status = 'Undone'
    else:
        task_status = 'Done'
    return render(request, 'task_detail.html', {'my_task': my_task, 'task_status': task_status})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from .utils import convert_hex_number_into_cyrilic
from main.decorators import unauthanticated_user
from .forms import ProfileForm
from main.models.user import User
from main.models.role import Role
from django.contrib.auth.decorators import login_required

# //TODO: In template files, views and urls change page name into better name
def main_page(request):
    convert = convert_hex_number_into_cyrilic('d093')
    return render(request, 'main.html', {
        'letter': convert,
    }) 

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
        form = UserCreationForm()
    return render(request, 'register_page.html', {
        'form': form
        })

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                role_id = form.cleaned_data['role']
                main_user = User(first_name=form.cleaned_data['first_name'], 
                                last_name=form.cleaned_data['last_name'], 
                                email=form.cleaned_data['email'], 
                                role=role_id, 
                                birth_date=form.cleaned_data['birth_date'], 
                                auth_user_id=request.user.id
                                )
                main_user.save()
                return redirect('main')
        else:
            form = ProfileForm()
        return render(request, 'profile.html', {
            'form': form
        })
    else:
        redirect('login')

#//TODO: Add functional to this pages: {--
@login_required
def calendar_page(request):
    return render(request, 'calendar_page.html')

def profile_page(request):
    my_profile = User.objects.filter(first_name=request.user)
    return render(request, 'own_profile.html', {
        'my_user': my_profile,
    })

def users(request):
    return render(request, 'users.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def event(request):
    return render(request, 'events.html')

def event_detail(request):
    return render(request, 'event_detail.html')
# --}

# Just password
"""
Admin12345!

7F@h3GNiPKeFbiZ
"""
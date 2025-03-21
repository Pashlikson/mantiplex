from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from .utils import convert_hex_number_into_cyrilic
from main.decorators import unauthanticated_user

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

#//TODO: custom register user
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
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'register_page.html', {
        'form':form,
        })

#//TODO: Add functional to this pages: {--
def calendar_page(request):
    return render(request, 'calendar_page.html')

def profile_page(request):
    my_profile = request.user
    return render(request, 'own_profile.html', {
        'my_user': my_profile,
    })

def event(request):
    return render(request, 'events.html')

def users(request):
    return render(request, 'users.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def event_detail(request):
    return render(request, 'event_detail.html')
# --}

# Just password
"""
Admin12345!
"""
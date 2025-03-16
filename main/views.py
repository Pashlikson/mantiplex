from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .utils import convert_hex_number_into_cyrilic

# Create your views here.
def main_page(request):
    convert = convert_hex_number_into_cyrilic('d093')
    return render(request, 'main.html', {
        'letter': convert,
    }) 

def login_page(request):
    if not request.user.is_authenticated:
        return redirect(request, 'register')
    else:
        if request.method == 'POST':
            password = request.POST['password']
            username = request.POST['username']
            user = authenticate(request, password=password, username=username)
            if user is not None:
                login(request, user)
                return redirect('calendar')
            else:
                return redirect('register')
        else:
            return render(request, 'login_page.html')

def register_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registeation Sucsedsful!"))
            return redirect('main')
    else:
        form = UserCreationForm()

    return render(request, 'register_page.html', {
        'form':form,
        })

def calendar_page(request):
    return render(request, 'calendar_page.html')

"""
Admin12345!
"""
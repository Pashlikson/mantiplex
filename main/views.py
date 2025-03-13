from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def main_page(request):
    return render(request, 'main.html') 

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        user = authenticate(request, username=username, email=email)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.success(request, ('Error at login'))
            return redirect('login')
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
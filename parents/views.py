from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def start_page(request):
    parent = User.objects.get(id=request.user.id)
    return render(request, 'parent_page.html', {'parent': parent})
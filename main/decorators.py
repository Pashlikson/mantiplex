from django.http import Http404
from django.shortcuts import redirect

def unauthanticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func
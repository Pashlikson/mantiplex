from django.shortcuts import render, HttpResponse

# Create your views here.
def start_page(request):
    return HttpResponse('Hello, students!')
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/student/', views.student_profile, name='student'),
    path('profile/parent/', views.parent_profile, name='parent'),
    path('profile/teacher/', views.teacher_profile, name='teacher'),
    path('register/', views.register_page, name='register'),
    path('calendar/', views.calendar_page, name='calendar'),
    path('calendar/your_profile/', views.profile_page, name='profile_page'),
    path('calendar/events_1st_march/', views.event, name='event'),
    path('calendar/users/', views.users, name='users'), 
    path('calendar/users/user_profile/', views.user_profile, name='user_profile'),
    path('calendar/events_1st_march/event_detail/', views.event_detail, name='event_detail')
]

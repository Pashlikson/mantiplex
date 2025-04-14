from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main'),
    path('login/', views.login_page, name='login'),
    path('accounts/login/', views.login_page, name='another_login'),
    path('profile/', views.profile, name='profile'),
    path('profile/student/', views.student_profile, name='student'),
    path('profile/parent/', views.parent_profile, name='parent'),
    path('profile/teacher/', views.teacher_profile, name='teacher'),
    path('register/', views.register_page, name='register'),
    path('calendar/', views.calendar_page, name='calendar'),
    path('calendar/your_profile/', views.profile_page, name='profile_page'),
    path('calendar/users/', views.users, name='users'),
    path('calendar/users/<int:id>/', views.user_profile, name='user_profile'),
    path('calendar/event/', views.event, name='event'),
    path('calendar/event/<int:id>/', views.event_detail, name='event_detail'),
    # path('calendar/events_1st_march/my_task/<int:id>/', views.task_detail, name='task_detail'),
    # path('calendar/event/add_event/', views.add_event, name='add_event'),
    # path('calendar/event/change_event/<int:id>/', views.change_event, name='change_event'),

    # path('/event', views.event, name='event'),
]

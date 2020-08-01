from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('users/register', views.register, name='register'),
    path('users/login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('users/logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('users/profile', views.profile, name='profile'),
    path('', views.doctors, name='doctors'),
    path('doctors/<slug:slug>/', views.doctor_detail, name='doctor-detail'),

    # api urls
    
]

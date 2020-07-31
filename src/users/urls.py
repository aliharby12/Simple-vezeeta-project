from django.urls import path
from . import views
urlpatterns = [
    path('doctors', views.doctors, name='doctors'),
    path('doctors/<slug:slug>/', views.doctor_detail, name='doctor-detail'),
]

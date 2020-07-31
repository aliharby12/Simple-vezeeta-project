from django.shortcuts import render
from .models import Profile

def doctors(request):
    """create a view to list all doctors"""
    doctors = Profile.objects.all()
    context = {'doctors':doctors}
    return render(request, 'doctors/doctors.html', context)

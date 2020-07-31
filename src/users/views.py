from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Profile

def doctors(request):
    """create a view to list all doctors"""
    doctors = Profile.objects.all()
    context = {'doctors':doctors}
    return render(request, 'doctors/doctors.html', context)

def doctor_detail(request, slug):
    """create view to render doctor detail"""
    doctor = get_object_or_404(Profile, slug=slug)
    return render(request, 'doctors/doctor-detail.html', {'doctor':doctor})

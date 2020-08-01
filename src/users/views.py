from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Profile
from .forms import UsercreationForm

def doctors(request):
    """create a view to list all doctors"""
    doctors = Profile.objects.all()
    context = {'doctors':doctors}
    return render(request, 'doctors/doctors.html', context)

def doctor_detail(request, slug):
    """create view to render doctor detail"""
    doctor = get_object_or_404(Profile, slug=slug)
    return render(request, 'doctors/doctor-detail.html', {'doctor':doctor})

def register(request):
    """create a register method"""
    if request.method == 'POST':
        form = UsercreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} لقد تم تسجيل الحساب بنجاح يا  !')
            return redirect('doctors')
    form = UsercreationForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)

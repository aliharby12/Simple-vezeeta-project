from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Profile, Comment
from .forms import (UsercreationForm, NewCommentForm,
                    UpdateUserForm, UpdateProfileForm,
                    ReservationForm
                    )
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def doctors(request):
    """create a view to list all doctors"""
    doctors = Profile.objects.all()
    context = {'doctors':doctors}
    return render(request, 'doctors/doctors.html', context)

def doctor_detail(request, slug):
    """create view to render doctor detail"""
    doctor = get_object_or_404(Profile, slug=slug)
    comments = doctor.comments.filter(active=True)
    comment_numbers = comments.count()
    comment_form = NewCommentForm()
    reserve_form = ReservationForm()

    # validate the comment form
    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.doctor = doctor
            new_comment.save()
            return redirect('doctor_detail', slug=profile.slug)
    else:
        comment_form = NewCommentForm()

    if request.method == 'POST':
        reserve_form = ReservationForm(request.POST)
        if reserve_form.is_valid():
            new_reserve = reserve_form.save(commit=False)
            new_reserve.doctor = doctor
            new_reserve.save()
            reserve_form = ReservationForm()
    else:
        reserve_form = ReservationForm()


    context = {'doctor':doctor, 'comments':comments,
               'comment_numbers':comment_numbers,
               'comment_form':comment_form,
               'reserve_form':reserve_form}
    return render(request, 'doctors/doctor-detail.html', context)

def register(request):
    """create a register method"""
    if request.method == 'POST':
        form = UsercreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} لقد تم تسجيل الحساب بنجاح يا  !')
            return redirect('login')
    form = UsercreationForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)

@login_required(login_url = 'login')
def profile(request):
    """create a view to edit my profile data"""
    user_form = UpdateUserForm(instance=request.user)
    profile_form = UpdateProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid and profile_form.is_valid:
            user_form.save()
            profile_form.save()
            return redirect('doctors')

    context = {'user_form':user_form, 'profile_form':profile_form}
    return render(request, 'users/profile.html', context)

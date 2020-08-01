from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Profile


class UsercreationForm(UserCreationForm):
    """create a form to register new user"""
    username = forms.CharField(label='اسم المستخدم')
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UpdateUserForm(forms.ModelForm):
    """create a form to edit user detail"""
    first_name = forms.CharField(label='الاسم الاول')
    last_name = forms.CharField(label='الاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class UpdateProfileForm(forms.ModelForm):
    """create a form to edit profile data"""
    class Meta:
        model = Profile
        fields = ('name', 'description', 'address',
                  'address_detail', 'phone', 'working_hours',
                  'Waiting_time', 'facebook', 'twitter',
                  'price', 'image', 'Specialist_doctor')

from django.contrib import admin
from .models import Profile, Comment, Reservation

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Reservation)

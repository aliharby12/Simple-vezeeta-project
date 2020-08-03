from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('profiles', views.ProfileView)
router.register('comments', views.CommentView)
router.register('reservation', views.ReservationView)


urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from . import views


urlpatterns = [
    path("profile/", views.profile, name="user_profile"),
    path("home/", views.home, name="user_home"),
]

from django.urls import include, path
from . import views

urlpatterns = [

    # register url
    path('register/', views.register, name="register"),
    
    # all other auth urls
    path('', include('django.contrib.auth.urls')),
]

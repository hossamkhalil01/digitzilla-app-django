from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import User


@login_required
def profile(request):
    # pass the current user
    return render(request, 'user/profile.html', {'current_user': request.user})

@login_required
def home (request):
    # pass the current user
    return render(request, 'user/home.html', {'current_user': request.user})

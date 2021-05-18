from .forms import RegistrationForm
from django.shortcuts import redirect, render

def register(request):

    form = RegistrationForm(request.POST or None)

    if form and form.is_valid():
        user = form.save()
        return redirect("login")

    return render(request, "registration/register.html", {"form": form})

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .forms import UserRegisterForm, UserUpdateForm
from .models.geouser import GeoUser


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Witaj {username}, zostałeś zarejestrowany!")
            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


class UserUpdate(UpdateView, LoginRequiredMixin):
    model = GeoUser
    form_class = UserUpdateForm
    fields = ["username", "email", "phone_number", "first_name", "last_name"]
    template_name = "users/updateuser.html"

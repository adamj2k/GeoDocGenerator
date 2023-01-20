from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from .forms import UserRegisterForm, UserUpdateForm
from .models.geouser import GeoUser


class UserRegisterView(CreateView):
    model = GeoUser
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = "login"

    def form_valid(self, form):
        username = form.data.get("username")
        form.save()
        messages.success(self.request, f"{username} Zostałeś zarejestrowany!")
        return redirect(self.success_url)


class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = GeoUser
    form_class = UserUpdateForm
    template_name = "users/updateuser.html"

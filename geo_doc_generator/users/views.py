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

    def set_user_as_inactive(self, user):
        user.is_active = False
        user.save()

    def form_valid(self, form):
        username = form.data.get("username")
        new_user = form.save(commit=False)
        self.set_user_as_inactive(new_user)
        new_user.save()
        messages.success(
            self.request,
            f"{username} Zostałeś zarejestrowany! Poczekaj na aktywację konta",
        )
        return redirect(self.success_url)


class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = GeoUser
    form_class = UserUpdateForm
    template_name = "users/updateuser.html"

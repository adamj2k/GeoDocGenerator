from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models.geouser import GeoUser


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = GeoUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "first_name",
            "last_name",
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = GeoUser
        fields = ["username", "email", "phone_number", "first_name", "last_name"]

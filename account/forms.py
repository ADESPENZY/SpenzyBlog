from django.contrib.auth.forms import UserCreationForm
from .models import Account


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['email', 'username', 'password1', 'password2']

from django import forms
from .models import Profile, Account

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'email']  # Allow users to edit username and email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture', 'phone_number', 'address', 'city', 'country']

    
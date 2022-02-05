from django import forms
from clients.models.models_clients import Clientstable
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clientstable
        exclude = ['insc']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

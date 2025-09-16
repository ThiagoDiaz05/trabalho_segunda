# register/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obrigatório. Digite um e-mail válido.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
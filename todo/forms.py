from django import forms
from . models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']
        labels = {
            "content": ""
        }

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {
            'username': None,
            'password': None,
            'password2': None
        }

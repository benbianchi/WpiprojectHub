#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms

import datetime

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'mdl-textfield__input', 'name': 'password'}))

    





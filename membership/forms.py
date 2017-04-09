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

    


# class ProfileForm(forms.Form):
#     skill = forms.ModelChoiceField(Skill.objects.all(),required=True, widget=forms.SelectMultiple(attrs={'class':'form-control'}),label="Select Skill(s):")    
#     major = forms.ModelChoiceField(Major.objects.all(),required=True, widget=forms.SelectMultiple(attrs={'class':'form-control'}),label="Select Major(s):")
#     bio = forms.CharField(label="Please enter a bio below for professors to read when you apply to a projects:",widget=forms.Textarea(attrs={'class':'form-control'}))  




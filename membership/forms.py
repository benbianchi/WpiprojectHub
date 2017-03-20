#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from .models import Major, Skill

# If you don't do this you cannot use Bootstrap CSS
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class ProfileForm(forms.Form):
    

    skill = forms.ModelChoiceField(Skill.objects.all(),required=True, widget=forms.SelectMultiple(attrs={'class':'form-control'}),label="Select Skill(s):")    

    major = forms.ModelChoiceField(Major.objects.all(),required=True, widget=forms.SelectMultiple(attrs={'class':'form-control'}),label="Select Major(s):")
    bio = forms.CharField(label="Please enter a bio below for professors to read when you apply to a projects:",widget=forms.Textarea(attrs={'class':'form-control'}))  


class ProjectForm(forms.Form):
    projectName= forms.CharField(max_length=50,label="Project Name:",widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    projectTagLine= forms.CharField(max_length=100, label="Project Tag line:",widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))

    projectDescription= forms.CharField(label="Please enter a description of the project below for students to read:",widget=forms.Textarea(attrs={'class':'form-control'}))  
    skill = forms.ModelChoiceField(Skill.objects.all(),required=True, widget=forms.SelectMultiple(attrs={'class':'form-control'}),label="Select Skill(s):")    
    major = forms.ModelChoiceField(Major.objects.all(),required=True, widget=forms.SelectMultiple(attrs={'class':'form-control'}),label="Select Major(s):")


    projectBeginDate = forms.DateInput()
    projectEndDate = forms.DateInput()
    projectDuration = forms.DateInput()

    
#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from models import Major, Skill, Project
import datetime

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


class SignUpForm(forms.Form):
    #Username, Password, Confirm Password, First, Last, Email
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
    passwordConfirmation = forms.CharField(label="Confirm Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))
    firstName = forms.CharField(label="First Name", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))
    lastName = forms.CharField(label="Last Name", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['projectName', 'projectTagLine', 'projectDescription', 'projectSkills', 'projectMajor', 'projectBeginDate', 'projectEndDate', 'projectDuration' ]
        widgets = {

            'projectName': forms.TextInput(attrs={'class': 'form-control'}),
            'projectTagLine':  forms.TextInput(attrs={'class': 'form-control'}),
            'projectDescription': forms.Textarea(attrs={'class':'form-control'}),
            'projectSkills': forms.CheckboxSelectMultiple(attrs={'class': ''}),
            'projectMajor':forms.CheckboxSelectMultiple(attrs={'class': ''}),
            'projectBeginDate':forms.SelectDateWidget(attrs={'class':'form-control'}),
            'projectEndDate': forms.SelectDateWidget(attrs={'class':'form-control'}),
            'projectDuration':forms.TextInput(attrs={'class':'form-control'})
        }

        labels = {            
            'projectName': 'Project Title',
            'projectTagLine':  'Project Tag Line',
            'projectDescription': 'Project Description',
            'projectSkills': 'Required Skill(s)',
            'projectMajor': 'Required Major(s)',
            'projectBeginDate': 'Project Start Date',
            'projectEndDate': 'Project End Date',
            'projectDuration': 'Project Duration'
        }

        querysets= {
            'projectSkills' : Skill.objects.filter(),
            'projectMajor' : Major.objects.filter()
        }

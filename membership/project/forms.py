from django import forms
from .models import Skill, Major, Project

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
        querysets = {
                'projectSkills' : Skill.objects.filter(),
                'projectMajor' : Major.objects.filter()
            }
        fields = ['projectName', 'projectTagLine', 'projectDescription', 'projectSkills', 'projectMajor', 'projectBeginDate', 'projectEndDate', 'projectDuration' ]

   
from django import forms
from .models import Skill, Major, Project


class ProjectForm(forms.ModelForm):

    """
    Project Form is a form that allows a user to create and update a project.
    """
    def __init__(self, project=None, *args, **kwargs):
        super(ProjectForm, self ).__init__(*args, **kwargs)
    
    class Meta:
        model = Project
        fields = ['projectName', 'projectTagLine', 'projectDescription', 'projectSkills', 'projectMajor', 'projectBeginDate', 'projectEndDate', 'projectDuration' ]   
    
        widgets = {
                'projectName': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'pattern':'[A-Z,a-z, ]*'}),
                'projectTagLine':  forms.TextInput(attrs={'class': 'mdl-textfield__input'}),
                'projectDescription': forms.Textarea(attrs={'class':'mdl-textfield__input', 'rows':"1"}),
                'projectSkills': forms.CheckboxSelectMultiple(attrs={'class': 'mdl-checkbox__input'}),
                'projectMajor':forms.CheckboxSelectMultiple(attrs={'class': ''}),
                'projectBeginDate':forms.SelectDateWidget(attrs={'class':'mdl-selectfield mdl-js-selectfield'}),
                'projectEndDate': forms.SelectDateWidget(attrs={'class':'mdl-textfield__input'}),
                'projectDuration':forms.TextInput(attrs={'class':'mdl-textfield__input'})
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
        

   
class searchForm(forms.Form):
    
    fields = ProjectForm.Meta.fields;

    searchValue = forms.CharField(label="searchValue", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'mdl-textfield__input', 'name': 'username'}))
    searchField = forms.Select();

from django import forms
from .models import Profile
from membership.project.models import Skill, Major
class ProfileForm(forms.ModelForm):
    """ 
        Profile Form is a django ModelForm that allows users to edit their
        Skills, and Majors, and bio

        The Model used is a Profile.
    """
    def __init__(self, project=None, *args, **kwargs):
        super(ProfileForm, self ).__init__(*args, **kwargs) 

    class Meta:
        model = Profile

        fields = ["skills", "majors", "bio"]
        widgets= {
        'bio': forms.Textarea(attrs={'class':'mdl-textfield__input', 'rows':"1"}),
         'skills': forms.CheckboxSelectMultiple(attrs={'class': 'mdl-checkbox__input'}),
         'majors':forms.CheckboxSelectMultiple(attrs={'class': ''}),
        }
        querysets = {
                'skills' : Skill.objects.filter(),
                'majors' : Major.objects.filter()
            }
        



from django import forms
from .models import Profile
from membership.project.models import Skill, Major
class ProfileForm(forms.ModelForm):
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
        



from django.contrib.auth.models import User
from django.db import models
from membership.project.models import Major, Skill

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    majors = models.ManyToManyField(Major, blank=True);
    skills = models.ManyToManyField(Skill, blank=True);
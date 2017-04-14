from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


class Major(models.Model):
    MajorName = models.CharField(max_length=100)
    def __str__ (self):
        return self.MajorName;

class Skill(models.Model):
    SkillName = models.CharField(max_length=100)

    def __str__ (self):
        return self.SkillName;   


class Project(models.Model):
    projectAuthor = models.ForeignKey('auth.User')
    projectName= models.CharField(max_length=50)
    projectTagLine= models.CharField(max_length=100)
    projectDescription= models.TextField()
    
    projectMajor = models.ManyToManyField(Major, blank=True);
    projectSkills = models.ManyToManyField(Skill, blank=True);

    postDate = models.DateField(auto_now=True)
    projectBeginDate = models.DateField(blank=True, null=True)
    projectEndDate = models.DateField(blank=True, null=True)
    projectDuration = models.FloatField(null=True)
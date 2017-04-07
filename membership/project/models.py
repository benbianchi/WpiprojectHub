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

class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    majors = models.ManyToManyField(Major);
    skills = models.ManyToManyField(Skill);
    


class Project(models.Model):
    projectAuthor = models.ForeignKey('auth.User')
    projectName= models.CharField(max_length=50)
    projectTagLine= models.CharField(max_length=100)
    projectDescription= models.TextField()
    
    projectMajor = models.ManyToManyField(Major);
    projectSkills = models.ManyToManyField(Skill);


    projectBeginDate = models.DateField(null=True)
    projectEndDate = models.DateField(null=True)
    projectDuration = models.FloatField(null=True)
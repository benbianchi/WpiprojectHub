from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


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
    projectAuthor = models.OneToOneField(Member,on_delete=models.CASCADE,default=None)
    projectName= models.CharField(max_length=50)
    projectTagLine= models.CharField(max_length=100)
    projectDescription= models.TextField()
    
    projectMajor = models.ManyToManyField(Major);
    projectSkills = models.ManyToManyField(Skill);


    projectBeginDate = models.DateField()
    projectEndDate = models.DateField()
    projectDuration = models.FloatField()


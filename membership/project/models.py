from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models



class Major(models.Model):
    """
    Major is a model that is just a string, and represents a student's primary field of study

    attrs:
        MajorName: The name of the major.
    """
    MajorName = models.CharField(max_length=100)
    def __str__ (self):
        return self.MajorName;

class Skill(models.Model):
    """
    Skill is a model that is just a string, and represents a student's ability

    attrs:
        SkillName: The name of the skill.
    """
    SkillName = models.CharField(max_length=100)

    def __str__ (self):
        return self.SkillName;   


class Project(models.Model):
    """
    A Project is a model that advertises a job that can be completed.

    attrs:
        projectAuthor: The creator of the project
        projectName: The title of the Project
        projectTagLine: A short, one sentence description of the project
        projectDescription: a detailed summary of the project
        projectMajor: the majors that are needed by the project
        projectSkills: the skills that are needed 
        postDate: the day that the project was created
        projectBeginDate: the date the project will be started
        projectEndDate: the date the project will end.
        projectDuration: how long the duration of the project is.
    """
    projectAuthor = models.ForeignKey('membership.PJUser',default=None)
    projectName= models.CharField(max_length=50)
    projectTagLine= models.CharField(max_length=100)
    projectDescription= models.TextField()
    
    projectMajor = models.ManyToManyField(Major, blank=True);
    projectSkills = models.ManyToManyField(Skill, blank=True);

    postDate = models.DateField(auto_now=True)
    projectBeginDate = models.DateField(blank=True, null=True)
    projectEndDate = models.DateField(blank=True, null=True)
    projectDuration = models.FloatField(null=True)
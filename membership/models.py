from __future__ import unicode_literals

from django.db import models


# Create your models here.


from django.contrib.auth.models import AbstractUser

class Member(models.Model):
    user = models.oneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Project(models.Model):
    projectName= models.CharField(max_length=50)
    projectTagLine= models.CharField(max_length=100)
    projectDescription= models.TextField()

    projectBeginDate = models.DateField()
    projectEndDate = models.DateField()
    projectDuration = models.FloatField()

    
from django.contrib.auth.models import User
from django.db import models
from membership.project.models import Major, Skill
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True, related_name="user")
    bio = models.TextField(max_length=500)
    majors = models.ManyToManyField(Major, blank=True);
    skills = models.ManyToManyField(Skill, blank=True);

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
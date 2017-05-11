from django.contrib.auth.models import User
from django.db import models
from membership.project.models import Major, Skill
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    """
        Profile is an object that is tied to a user through a one-to-one relationship.
        Profiles are destroyed when a user is deleted.

        attrs:
            user: the user that the profile describes
            bio:  Some text that describes the User
            majors: The major(s) that the user has.
            skills: The skills(s) that the user has.
    """
    user = models.OneToOneField(User, unique=True, primary_key=True, related_name="user")
    bio = models.TextField(max_length=500)
    majors = models.ManyToManyField(Major, blank=True);
    skills = models.ManyToManyField(Skill, blank=True);


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
        A reciever that is called when a user is created/registered.
        This function fires after registration and takes the newly registered User
        and ties a newly created profile.
    """
    if created:
        Profile.objects.create(user=instance)
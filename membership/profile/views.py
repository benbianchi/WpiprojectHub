from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django import forms
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from .models import Profile
from .forms import ProfileForm
from django.views.generic.detail import DetailView
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileRead(LoginRequiredMixin, DetailView):
    """
    ProfileRead is a view that descends from Django.DetailView.
    Profile read allows a user to read the attributes of a profile.
    """
    model = Profile
    template_name = 'membership/profile.html'
        
   

class ProfileUpdate(UpdateView):
    """
    ProfileUpdate is a view that descends from UpdateView  
    This view allows the author of a Profile to edit and update old data with new values
    """
    model = Profile
    template_name = 'membership/update.html'
    form_class = ProfileForm
    def get_object(self, *args, **kwargs):
        obj = super(ProfileUpdate, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
             return HttpResponseForbidden() # TODO
        return obj

    def get_success_url(self):
        """
        Without changing the success url this way, we can only redirect to a static url.
        This allows us to redirect to the read page of the profile we have updated.
        """
        return reverse('profile', kwargs={"pk": self.object.user.id})
    
    def get_context_data(self, **kwargs):
        context = super(ProfileUpdate, self).get_context_data(**kwargs)
        return context

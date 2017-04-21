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

class ProfileRead(DetailView):

    model = Profile
    template_name = 'membership/profile.html'
        
    def get_context_data(self, **kwargs):
        context = super(ProfileRead, self).get_context_data(**kwargs)
        print context
        return context


class ProfileUpdate(UpdateView):
    model = Profile
    template_name = 'membership/update.html'
    form_class = ProfileForm
    def get_object(self, *args, **kwargs):
        obj = super(ProfileUpdate, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
             return HttpResponseForbidden() # TODO
        return obj

    def get_success_url(self):
        return reverse('profile', kwargs={"pk": self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super(ProfileUpdate, self).get_context_data(**kwargs)
        return context

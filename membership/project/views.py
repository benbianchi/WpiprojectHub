from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django import forms
from .models import Project, Skill, Major
from membership.profile.models import Profile
from .forms import ProjectForm, searchForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin




class ManageProjectView(LoginRequiredMixin, ListView):
    """
    ManageProjectView is a view that requires the user to be logged in and is a Django.ListView
    This view allows a user to see the projects that he has made.
    """
    template_name='membership/manage.html'
    model = Project
    def get_queryset(self):
        qs = super(ManageProjectView, self).get_queryset()
        return qs.filter(projectAuthor__exact=self.request.user)

class ProjectListView(ListView):
    """
    ProjectListView is a view that shows all projects sorted by project date.
    """
    model = Project
    template_name = 'discover.html'


class ProjectCreate(LoginRequiredMixin, CreateView):
    """
    ProjectCreate is a Django.CreateView which is the main way to generate a project.
    """
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm
    success_url="/discover/"
    fail_url="/"

    def form_valid(self, form):
        form.instance.projectAuthor = self.request.user
        return super(ProjectCreate, self).form_valid(form)


class ProjectRead(LoginRequiredMixin, DetailView):
    """
    ProjetRead descends from Django.DetailView and allows users to read the attributes of a project.
    """
    model = Project

    template_name = 'project/read.html'

    def get_context_data(self, **kwargs):
        """
        This function adds the profile of the user to the context of this view. We use this
        in the card at the bottom of the view.
        """
        context = super(ProjectRead, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(user__exact=self.request.user)
        return context


class ProjectUpdate(LoginRequiredMixin,UpdateView):
    """
    ProjectUpdate is a Django.UpdateView that requires a user to be Logged in.
    """
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    
    def get_object(self, *args, **kwargs):
        """
        This function prevents a user who is not the author, from using this view.
        """
        obj = super(ProjectUpdate, self).get_object(*args, **kwargs)
        if not obj.projectAuthor == self.request.user:
             raise PermissionDenied()
        return obj

    def get_success_url(self):
        """
        This function allows a succesful update to redirect to the read view of the project.
        """
        return reverse('project_read', kwargs={"pk": self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super(ProjectUpdate, self).get_context_data(**kwargs)
        return context


@login_required(login_url="/login/")
def ProjectDelete(request,num):

    def get_object(self, *args, **kwargs):
        """
        This function prevents a user from deleting another user's project.
        """
        obj = super(ProjectUpdate, self).get_object(*args, **kwargs)
        if not obj.projectAuthor == self.request.user:
             raise PermissionDenied()
        return obj

    p = get_object_or_404(Project,pk=num);
    p.delete();
    return redirect("discover")


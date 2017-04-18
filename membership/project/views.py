from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django import forms
from .models import Project, Skill, Major
from .forms import ProjectForm, searchForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin



    
class SearhableListView(LoginRequiredMixin, FormMixin, ListView):
    def get(self, request, *args, **kwargs):
        # From ProcessFormMixin
        form_class = self.get_form_class()
        self.form = self.get_form(form_class)

    template_name='membership/manage.html'
    def get_queryset(self):
        qs = super(ManageProjectView, self).get_queryset()
        return qs.filter(projectAuthor__exact=self.request.user)


class ManageProjectView(SearhableListView):
    form_class = searchForm
    model = Project

class ProjectListView(ListView):
    model = Project
    template_name = 'discover.html'


class ProjectCreate(LoginRequiredMixin,CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm
    success_url="/discover/"
    fail_url="/"

    def form_valid(self, form):
        form.instance.projectAuthor = self.request.user
        return super(ProjectCreate, self).form_valid(form)


class ProjectRead(DetailView):
    model = Project

    template_name = 'project/read.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectRead, self).get_context_data(**kwargs)
        return context


class ProjectUpdate(LoginRequiredMixin,UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    
    def get_object(self, *args, **kwargs):
        obj = super(ProjectUpdate, self).get_object(*args, **kwargs)
        if not obj.projectAuthor == self.request.user:
             raise PermissionDenied()
        return obj

    def get_success_url(self):
        return reverse('project_read', kwargs={"pk": self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super(ProjectUpdate, self).get_context_data(**kwargs)
        return context


@login_required(login_url="/login/")
def ProjectDelete(request,num):

    p = get_object_or_404(Project,pk=num);
    p.delete();
    return redirect("discover")


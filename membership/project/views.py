from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django import forms
from .models import Project, Skill, Major
from .forms import ProjectForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, redirect
from django.core.urlresolvers import reverse, reverse_lazy


class ProjectListView(ListView):
    model = Project
    template_name = 'discover.html'

class ProjectCreate(CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectForm
    success_url="/discover/"

    def form_valid(self, form):
        form.instance.projectAuthor = self.request.user
        return super(ProjectCreate, self).form_valid(form)



class ProjectRead(DetailView):
    model = Project

    template_name = 'project/read.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectRead, self).get_context_data(**kwargs)
        return context


class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm
    
    def get_success_url(self):
        return reverse('project_read', kwargs={"pk": self.object.id})
    
    def get_context_data(self, **kwargs):
        context = super(ProjectUpdate, self).get_context_data(**kwargs)
        return context



def ProjectDelete(request,num):

    p = get_object_or_404(Project,pk=num);
    p.delete();
    reverse_lazy("discover")


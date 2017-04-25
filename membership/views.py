from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .project.models import Project
from .profile.models import Profile
from .project.forms import searchForm
from django.views.generic.list import ListView
from django.http import QueryDict
from django.db.models import Q


def profileQueryOrNone(query):
        try:
                qlist =Profile.objects.filter(
                        Q(user__username__icontains=query) |
                        Q(bio__icontains=query) |
                        Q(skills__SkillName__icontains=query)  |
                        Q(majors__MajorName__icontains=query),
                )
        except Profile.DoesNotExist:
                return None;
        return qlist;

def projectQueryOrNone(query):
        try:
                qlist =Project.objects.filter(
                        Q(projectName__icontains=query) |
                        Q(projectTagLine__icontains=query) |
                        Q(projectDescription__icontains=query) |
                        # Q(projectMajor_MajorName__icontains=query) |
                        # Q(projectSkill_SkillName__icontains=query) |
                        Q(postDate__icontains=query) |
                        Q(projectBeginDate__icontains=query) |
                        Q(projectEndDate__icontains=query)
                )
        except Project.DoesNotExist:
                return None;
        return qlist;

class SearchListView(ListView):
        model = Project
        context_object_name = 'search_list'    
        template_name = 'search.html'

        
        def get_queryset(self, **kwargs):
                query = self.request.GET.get('q', None) 
                return projectQueryOrNone(query);

        def get_context_data(self, **kwargs):
                query = self.request.GET.get('q', None)                 
                context = super(SearchListView, self).get_context_data(**kwargs)
                context['profiles'] = profileQueryOrNone(query)
                
                return context


def home(request):
        return render(request, "home.html")

@login_required(login_url="/login/")
def discover(request):
        projects = Project.objects.filter().order_by('projectBeginDate')
        return render(request, "discover.html" ,{"projects": projects, 'searchForm': ProfileForm})

@login_required(login_url="/login/")
def profile(request):
        return render(request, "membership/profile.html", {'profile_form': ProfileForm})
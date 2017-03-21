from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from .forms import ProfileForm, ProjectForm
from .models import Project

def home(request):
        return render(request, "home.html")

@login_required(login_url="login/")
def discover(request):
        projects = Project.objects.filter().order_by('projectBeginDate')


        return render(request, "discover.html" ,{"projects": projects})

@login_required(login_url="login/")
def profile(request):
        return render(request, "membership/profile.html", {'profile_form': ProfileForm})

@login_required
def createProject(request):
        #Get and Posts
        if (request.method == "GET"):
                return render(request, "project/project.html", {"project_form": ProjectForm})

        if (request.method == "POST"):
                handleProjectOnPost(request)       

        return HttpResponseRedirect("/project")

@login_required(login_url="login/")
def viewExistingProject(request,num=None):
        if request.method == "GET":
                return lookUpExistingProject(request,num);
        
        if request.method == "POST":
                #Process form
                form = ProjectForm(request.POST)
                if (form.is_valid()):
                        print("Created")
                        p = Project()
                        p.author = request.user
                        p.save()
                else:
                        print("\nForm aint valid\n")
                handleProjectUpdate(request,num)
        return HttpResponseRedirect("/project")

def handleProjectUpdate(request,num):
        pj = get_object_or_404(Project, pk=num)

        print("lookup Successful.")
        form = ProjectForm(request.POST)

        if (form.is_valid()):
                print("Form Validation Successful.")
                pj = form.save(commit=False)
                pj.projectAuthor = request.user
                pj.save();
        else:
                print("\nForm aint valid\n"+str(form.errors))
        

def handleProjectOnPost(request):

        form = ProjectForm(request.POST)
        
        if (form.is_valid()):                
                
                newProject = form.save(commit=False)
                newProject.projectAuthor = request.user        
                newProject.save();

                print("Successfully Saved")

        else:
                print("\nForm aint valid\n"+str(form.errors))


def lookUpExistingProject(request, num):
        pj = get_object_or_404(Project, pk=num)
        projectForm = ProjectForm(instance=pj)
        return render(request,"project/project.html", {"project_form": projectForm, "project":pj })

def attemptDelete(request,num):
        pj = get_object_or_404(Project, pk=num)

        if (pj.projectAuthor == request.user):
                pj.delete()
                return render(request,"project/delete.html");
        else:
                return render(request,"unauthorized.html");
        
        
        
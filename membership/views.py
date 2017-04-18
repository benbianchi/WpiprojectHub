from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .project.models import Project
from .project.forms import searchForm



def home(request):
        return render(request, "home.html")

@login_required(login_url="/login/")
def discover(request):
        projects = Project.objects.filter().order_by('projectBeginDate')


        return render(request, "discover.html" ,{"projects": projects, "searchForm": searchForm})

@login_required(login_url="/login/")
def profile(request):
        return render(request, "membership/profile.html", {'profile_form': ProfileForm})


        
# #Create Read Update Delete
# @login_required(login_url="/login/")
# def projectRead(request,num):
#         if (request.method == "GET"):
#                 return lookUpExistingProject(request,num);
#         else:
#                 return projectUpdate(request,num);
# @login_required(login_url="/login/")
# def projectCreate(request):
#         f = ProjectForm(request.POST)
        
#         newProject = f.save(commit=False)
#         newProject.projectAuthor = request.user        
#         newProject.save();

#         assembleProject(request,f, newProject)

        
#         print("Successfully Saved")
#         return redirect("/discover/")


# @login_required(login_url="/login/")
# def projectUpdate(request,num):
#         pj = get_object_or_404(Project, pk=num)
#         projectForm = ProjectForm(request.POST)  
        

#         assembleProject(request,projectForm,pj)
#         pj.save();
        
#         return redirect("/project/"+str(pj.id))



# @login_required(login_url="/login/")
# def projectDelete(request,num):
#         pj = get_object_or_404(Project, pk=num)

#         if (pj.projectAuthor == request.user):
#                 pj.delete()
#                 return render(request,"project/delete.html");
#         else:
#                 return render(request,"unauthorized.html");

# @login_required(login_url="/login/")        
# def assembleProject(request,form, pj):
#         if (form.is_valid()):
#                 pj.projectSkills = form.cleaned_data['projectSkills']
#                 pj.projectMajor = form.cleaned_data['projectMajor']
#                 pj.projectAuthor = request.user
#                 print "Form Populated."
#         else:
#                 print("\nForm aint valid\n"+str(form.errors))

# @login_required(login_url="/login/")
# def lookUpExistingProject(request, num):

#         pj = get_object_or_404(Project, pk=num)
#         projectForm = ProjectForm(instance=pj)        
#         return render(request,"project/project.html", {"project_form": projectForm, "project":pj })

# @login_required(login_url="/login/")


# @login_required(login_url="/login/")
# def manageProjects(request):
#         projects = Project.objects.filter(projectAuthor__exact=request.user)


#         return render(request, "membership/manage.html" ,{"projects": projects})
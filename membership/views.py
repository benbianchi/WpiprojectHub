from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from forms import ProfileForm, ProjectForm
from django.contrib.auth.decorators import login_required

def home(request):
        return render(request, "home.html")

@login_required(login_url="login/")
def dashboard(request):
        return render(request, "dashboard.html")

@login_required(login_url="login/")
def profile(request):
        return render(request, "membership/profile.html", {'profile_form': ProfileForm})

@login_required(login_url="login/")
def inspectProject(request):
        if request.method == "GET":
                return render(request, "project/project.html", {"project_form": ProjectForm})
        if request.method == "POST":
                #Process form
                form = ProjectForm(request.POST)
                if (form.is_valid()):
                        print "Created"
                        p = Project()
                        p.author = request.user
                        p.save()
                else:
                        print "\nForm aint valid\n"
        return HttpResponseRedirect("/project")


# def onMembershipUpdate(request, pk):
        
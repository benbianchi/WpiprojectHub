# log/urls.py
from django.conf.urls import url
from . import views
from forms import ProfileForm

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^discover/$', views.discover, name='discover'),

    url(r'^project/(?P<num>[0-9]+)$', views.viewExistingProject, name='project'),
        url(r'^project/(?P<num>[0-9]+)/delete/$', views.attemptDelete, name='project'),
    url(r'^project/$', views.createProject, name='project'),
    
    url(r'^profile/$', views.profile, name="profile"),
]
# log/urls.py
from django.conf.urls import url
from . import views
from project.views import *


# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^discover/$', ProjectListView.as_view(), name='discover'),
    

    #Project CRUD
    # url(r'^project/$', views.projectHome, name='project'),
    url(r'^project/create$', ProjectCreate.as_view(), name='Create Project'),
    url(r'^project/(?P<pk>[0-9]+)$', ProjectRead.as_view(), name='Project'),
    url(r'^project/(?P<pk>[0-9]+)/edit$', ProjectUpdate.as_view(), name='Project'),
    url(r'^project/(?P<pk>[0-9]+)/delete$', ProjectDelete.as_view(), name='Project'),
    # url(r'^project/(?P<num>[0-9]+)/delete/$', views.projectDelete, name='project'),
    url(r'^profile/$', views.profile, name="profile"),

    #Manage Project URL
    # url(r'^manage/$', views.manageProjects, name='project'),
]
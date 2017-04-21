# log/urls.py
from django.conf.urls import url
from . import views
from membership.project.views import *
from membership.profile.views import *
from membership.views import SearchListView
# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^discover/$', ProjectListView.as_view(), name='discover'),
    

    #Project CRUD
    # url(r'^project/$', views.projectHome, name='project'),
    url(r'^project/create$', ProjectCreate.as_view(), name='create_project'),
    url(r'^project/(?P<pk>[0-9]+)$', ProjectRead.as_view(), name='project_read'),
    url(r'^project/(?P<pk>[0-9]+)/edit$', ProjectUpdate.as_view(), name='project_update'),
    url(r'^project/(?P<num>[0-9]+)/delete$', ProjectDelete, name='project_delete'),
    
    
    #Profile CRUD
    url(r'^profile/(?P<pk>[0-9]+)$', ProfileRead.as_view(), name="profile"),
    url(r'^profile/(?P<pk>[0-9]+)/edit$', ProfileUpdate.as_view(), name="profile_edit"),
    
    #Manage Project URL
    url(r'^manage/$', ManageProjectView.as_view(), name='project'),

    #Manage Search URL
    url(r'^search/$', SearchListView.as_view(), name='search'),
]
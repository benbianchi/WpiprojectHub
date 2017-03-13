# log/urls.py
from django.conf.urls import url
from . import views
from forms import ProfileForm

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^project/$', views.inspectProject, name='project'),
    url(r'^profile/$', views.profile, name="profile"),
]
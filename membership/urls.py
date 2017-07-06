# membership/urls.py
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from .views import LoginView
from membership.user.views import PJUserViewSet


router = routers.SimpleRouter()
router.register(r'users', PJUserViewSet)


# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^discover/$', views.discover, name='home'),
    url(r'^login/$', views.login, name='discover'),
    url(r'^api/login/$',LoginView),
    url(r'^api/', include("membership.project.urls")),
    url(r'^api/', include(router.urls)),
    



]
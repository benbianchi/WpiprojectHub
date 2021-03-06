"""projectHub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from membership.forms import LoginForm


urlpatterns = [
    url(r'^admin/', admin.site.urls),       #
    url(r'', include('membership.urls')),
    url(r'^login/$', views.login, {'template_name': 'registration/login.html', 'authentication_form': LoginForm}, name="login"),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),  

    # Registration using middle-ware
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # We will migrate to use hmac at a later date.
    # url(r'^accounts/', include('registration.backends.hmac.urls')),

]

from django.conf.urls import url, include
from . import views
from rest_framework import routers
from .views import ProjectViewSet

router = routers.SimpleRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]

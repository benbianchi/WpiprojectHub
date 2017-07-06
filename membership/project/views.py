from rest_framework import permissions, viewsets
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Project
from .permissions import IsUserProjectAuthor
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.order_by('postDate')
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(), IsUserProjectAuthor(),)

def perform_create(self, serializer):
    instance = serializer.save(author=self.request.user)

    return super(ProjectViewSet, self).perform_create(serializer)



class AccountProjectsViewSet(viewsets.ViewSet):
    queryset = Project.objects.select_related('author').all()
    serializer_class = ProjectSerializer

    def list(self, request, account_username=None):
        queryset = self.queryset.filter(author__username=account_username)
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
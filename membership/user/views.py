from rest_framework import permissions, viewsets
from django.http import HttpResponse, HttpResponseBadRequest
from membership.models import PJUser
from membership.user.permissions import IsPJUserOwner
from membership.user.serializers import PJUserSerializer


class PJUserViewSet(viewsets.ModelViewSet):
    lookup_field = 'email'
    queryset = PJUser.objects.all()
    serializer_class = PJUserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsPJUserOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            PJUser.objects.create_user(**serializer.validated_data)

            return HttpResponse("User Succesfully Created")

        print(serializer.errors)
        return HttpResponseBadRequest({'User could not be created with received data.'
        })



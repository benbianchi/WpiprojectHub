# membership/views.py

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from rest_framework import status, views
from rest_framework.response import Response


def home(request):
    return render(request, "home.html")


def discover(request):
    return render(request, "pages/discover.html")

    import json

def login(request):
    return render(request, template_name='pages/login.html')

class LoginView(views.APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)

        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = AccountSerializer(account)

                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)
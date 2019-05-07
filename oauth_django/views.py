from django.shortcuts import render


# Create your views here.
from django.shortcuts import render
from .models import Mensaje
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from rest_framework import viewsets
from . import serializers
from django.contrib.auth import models


def index(request):
    context = {
        'posts': Mensaje.objects.order_by('-date')
        if request.user.is_authenticated else []
    }

    return render(request, 'index.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
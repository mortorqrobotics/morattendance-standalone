from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from server.apps.main import models
from . import serializers

# Create your views here.


class HourViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticated,)
    queryset = models.Hour.objects.all()
    serializer_class = serializers.HourSerializer

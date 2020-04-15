from django.shortcuts import render
from rest_framework import viewsets
from .models import Chela
from .serializers import ChelaSerializers


class ChelaViewSet(viewsets.ModelViewSet):
    serializer_class = ChelaSerializers
    queryset = Chela.objects.all()
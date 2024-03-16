from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ProjectSerializer, ShiftSerializer
from projects.models import Project
from shifts.models import Shift


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

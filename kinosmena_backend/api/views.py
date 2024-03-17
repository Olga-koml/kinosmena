from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ProjectSerializer, ShiftSerializer
from projects.models import Project
from shifts.models import Shift


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Представление для проектов.

    Позволяет получать, создавать, редактировать, удалять проект.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ShiftViewSet(viewsets.ModelViewSet):
    """
    Представление для смен.

    Позволяет получать, создавать, редактировать, удалять смену.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

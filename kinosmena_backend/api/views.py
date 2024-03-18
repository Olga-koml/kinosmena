from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ProjectSerializer
from projects.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Представление для проектов.

    Позволяет получать, создавать, редактировать, удалять проект.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


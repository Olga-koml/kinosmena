from django.shortcuts import render

from rest_framework import viewsets
from projects.serializers import ProjectSerializer
from projects.models import Project
from users.models import TelegramUser
from django_filters.rest_framework import DjangoFilterBackend
# from .filters import ProjectFilter
from api import schemas
from drf_yasg.utils import swagger_auto_schema


def get_user_tid(request):
    tid = request.GET.get('tid')
    user, create = TelegramUser.objects.get_or_create(
        tid=tid
    )

    return user


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Представление для проектов.

    Позволяет получать, создавать, редактировать, удалять проект.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ['is_archive',]
    # filterset_class = ProjectFilter

    def get_queryset(self):
        user: TelegramUser = get_user_tid(request=self.request)
        return user.projects.all()

    def perform_create(self, serializer):
        user: TelegramUser = get_user_tid(request=self.request)
        serializer.save(user=user)
    # def get_queryset(self):
    #     user = self.request.user
    #     return user.projects.all()

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    @swagger_auto_schema(
        manual_parameters=schemas.archive_project_filter_param
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

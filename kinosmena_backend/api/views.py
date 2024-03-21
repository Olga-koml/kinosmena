from django.shortcuts import render

from rest_framework import viewsets
from .serializers import ProjectSerializer
from projects.models import Project
from users.models import TelegramUser


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

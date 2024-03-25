from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.exceptions import PermissionDenied

from projects.models import Project
from users.models import TelegramUser


class IsProjectOwner(BasePermission):
    """
    Проверка, является ли пользователь создателем проекта.
    """

    def has_permission(self, request, view):
        if 'tid' in request.GET and request.method == 'POST' and request.data.get('project'):
            user_id = request.GET.get('tid')
            user = TelegramUser.objects.get(tid=user_id)
            project = Project.objects.get(id=request.data.get('project'))
            if project.user != user:
                raise PermissionDenied("Вы не являетесь владельцем проекта.")
            return True
        if request.method in SAFE_METHODS:
            return True

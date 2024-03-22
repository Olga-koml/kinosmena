from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet

from projects.models import Project
from shifts.filters import ShiftFilter
from shifts.models import Shift
from shifts.permissions import IsProjectOwner
from shifts.serializers import ShiftSerializer
from users.models import TelegramUser


class ShiftViewSet(ModelViewSet):
    """
    Представление для смен.

    Позволяет получать, создавать, редактировать, удалять смену.
    """
    serializer_class = ShiftSerializer
    filterset_class = ShiftFilter
    filter_backends = (filters.DjangoFilterBackend, )
    permission_classes = [IsProjectOwner]
    filterset_fields = [
        'project',
        'user',
        'start_date_from',
        'start_date_to',
    ]

    def get_queryset(self):
        user, created = TelegramUser.objects.get_or_create(
            tid=self.request.GET.get('tid')
        )
        return user.shifts.all()

    def perform_create(self, serializer):
        user, created = TelegramUser.objects.get_or_create(
            tid=self.request.GET.get('tid')
        )
        project = Project.objects.get(
            id=self.request.data.get('project')
        )
        active_shifts = Shift.objects.filter(
            user=user,
            end_date__isnull=True,
            project=project
        )
        if active_shifts:
            raise ValueError(f'Незавершенная смена: {active_shifts[0].id}')
        serializer.validated_data['user'] = user
        serializer.save()

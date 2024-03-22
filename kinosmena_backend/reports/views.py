from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from projects.models import Project
from reports.filters import ReportFilter
from reports.models import Report
from reports.permissions import IsProjectOwner
from reports.serializers import ReportSerializer
from users.models import TelegramUser


class ReportViewSet(ModelViewSet):
    """
    Представление для смен.

    Позволяет получать, создавать, редактировать, удалять смену.
    """
    serializer_class = ReportSerializer
    # queryset = Report.objects.all()
    filterset_class = ReportFilter
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
        return user.reports.all()

    def perform_create(self, serializer):
        user, created = TelegramUser.objects.get_or_create(
            tid=self.request.GET.get('tid')
        )
        project = Project.objects.get(
            id=self.request.data.get('project')
        )
        active_shifts = Report.objects.filter(
            user=user,
            end_date__isnull=True,
            project=project
        )
        if active_shifts:
            raise ValueError(f'Незавершенная смена: {active_shifts[0].id}')
        serializer.validated_data['user'] = user
        serializer.save()

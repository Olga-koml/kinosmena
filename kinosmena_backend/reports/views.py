from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from django_filters import rest_framework as filters

from projects.models import Project
from reports.models import Report
from reports.serializers import ReportSerializer
from users.models import TelegramUser


def get_user_tid(request):
    tid = request.GET.get('tid')
    user, create = TelegramUser.objects.get_or_create(
        tid=tid
    )

    return user


class ReportViewSet(ModelViewSet):
    """
    Представление для смен.

    Позволяет получать, создавать, редактировать, удалять смену.
    """
    serializer_class = ReportSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_fields = [
            'project',
            'user',
            'start_date',
            'end_date'
        ]

    def get_queryset(self):
        user: TelegramUser = get_user_tid(request=self.request)
        queryset = Report.objects.filter(
            user=user
        )

        return queryset

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            self.get_queryset().filter(
                end_date__isnull=False
            ), many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        user, created = TelegramUser.objects.get_or_create(
            tid=self.request.data.get('user')
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
        serializer.save()

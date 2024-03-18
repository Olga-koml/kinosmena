from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

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

    def get_queryset(self):
        user: TelegramUser = get_user_tid(request=self.request)
        queryset = Report.objects.filter(
            end_date__isnull=False,
            user__tid=user.tid
        )

        return queryset

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

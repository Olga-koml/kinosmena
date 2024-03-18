from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shifts.models import Shift
from shifts.serializers import ShiftSerializer
from users.models import TelegramUser


def get_user_tid(request):
    tid = request.GET.get('tid')
    user, create = TelegramUser.objects.get_or_create(
        tid=tid
    )

    return user


class ShiftViewSet(ModelViewSet):
    """
    Представление для смен.

    Позволяет получать, создавать, редактировать, удалять смену.
    """
    serializer_class = ShiftSerializer

    def get_queryset(self):
        user: TelegramUser = get_user_tid(request=self.request)
        queryset = Shift.objects.filter(user__id=user.tid)

        return queryset

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

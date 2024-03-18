from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from shifts.models import Shift
from shifts.serializers import ShiftSerializer


class ShiftViewSet(ModelViewSet):
    """
    Представление для смен.

    Позволяет получать, создавать, редактировать, удалять смену.
    """
    serializer_class = ShiftSerializer

    def get_queryset(self):
        telegram_id = self.request.GET.get('id')
        queryset = Shift.objects.filter(user__id=telegram_id)

        return queryset

    def list(self, request, *args, **kwargs):

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)


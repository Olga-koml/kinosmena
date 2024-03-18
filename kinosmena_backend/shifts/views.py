from rest_framework.viewsets import ModelViewSet

from shifts.models import Shift
from shifts.serializers import ShiftSerializer


class ShiftViewSet(ModelViewSet):
    """
    Представление для смен.

    Позволяет получать, создавать, редактировать, удалять смену.
    """
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer

    def get(self, request):
        telegram_id = request.GET.get('id')
        print(telegram_id)
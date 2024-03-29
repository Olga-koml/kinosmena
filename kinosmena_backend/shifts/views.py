from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from rest_framework.decorators import action

from projects.models import Project
from shifts.filters import ShiftFilter
from shifts.models import Shift
from shifts.permissions import IsProjectOwner
from shifts.serializers import ShiftSerializer
from users.models import TelegramUser
from shifts.config import load_config
from api import schemas
from drf_yasg.utils import swagger_auto_schema
from shifts.export_reports import get_export_shifts_to_excel

config = load_config()


class ShiftViewSet(ModelViewSet):
    """
    Представление для смен.

    Позволяет получать, создавать, редактировать, удалять смену.
    """
    serializer_class = ShiftSerializer
    filterset_class = ShiftFilter
    filter_backends = (filters.DjangoFilterBackend, )
    # permission_classes = [IsProjectOwner]

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
            raise serializers.ValidationError({'details': f'{config.active_shift_error}, shift_id: {active_shifts[0].id}'})
        serializer.validated_data['user'] = user
        serializer.save()

    @action(
        detail=False,
        # permission_classes=[IsAuthenticated]
    )
    def export_shifts_to_excel(self, request):
        return get_export_shifts_to_excel(request)

    @swagger_auto_schema(
        manual_parameters=schemas.shifts_filter_params
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

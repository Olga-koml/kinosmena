from rest_framework.viewsets import ModelViewSet

from services.models import Service
from services.serializers import ServicesSerializer


class ServicesView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer

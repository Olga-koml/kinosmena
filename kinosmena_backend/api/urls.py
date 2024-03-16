from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ProjectViewSet, ShiftViewSet


router = DefaultRouter()

router.register(r'projects', ProjectViewSet, basename='projects')
router.register(r'shifts', ShiftViewSet, basename='shifts')

urlpatterns = [
    path('', include(router.urls)),
]

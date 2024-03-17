from django.contrib import admin
from django.urls import include, path

from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += doc_urls

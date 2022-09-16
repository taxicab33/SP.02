from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('equipment.urls')),
    path('', include('accounts.urls')),
    path('', include('expendable_materials.urls')),
    path('', include('programs.urls')),
    path('', include('network_settings.urls')),
    path('', include('inventory.urls')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
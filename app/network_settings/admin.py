from django.contrib import admin

from network_settings.models import NetworkSettings


@admin.register(NetworkSettings)
class NetworkSettingsAdmin(admin.ModelAdmin):
    list_display = ('ip_address',
                    'mask',
                    'main_gate',
                    'dns',
                    'equipment')

from django.contrib import admin

from developers.models import Developer


@admin.register(Developer)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', )

from django.contrib import admin
from equipment.models import *

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('inventory_number',
                    'classroom',
                    'name',
                    'price',
                    'status',
                    'model',
                    'type',
                    'resp_user',
                    'temp_resp_user',)

admin.site.register(EquipmentType)

@admin.register(EquipmentClassroomHistory)
class EquipmentClassroomHistoryAdmin(admin.ModelAdmin):
    list_display = ('equipment',
                    'classroom',
                    'datetime')


@admin.register(EquipmentRespUserHistory)
class EquipmentRespUserHistoryHistoryAdmin(admin.ModelAdmin):
    list_display = ('equipment',
                    'resp_user',
                    'datetime')
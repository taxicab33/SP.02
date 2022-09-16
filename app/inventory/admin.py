from django.contrib import admin
from inventory.models import Inventory, InventoryedEquipment


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'start_date',
                    'end_date')


@admin.register(InventoryedEquipment)
class InventoryedEquipmentAdmin(admin.ModelAdmin):
    list_display = ('inventory',
                    'equipment',
                    'comment',
                    'inventory_time')
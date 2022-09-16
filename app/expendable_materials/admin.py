from django.contrib import admin

from expendable_materials.models import *


@admin.register(ExpendableMaterialType)
class ExpendableMaterialTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(ExpendableMaterial)
class ExpendableMaterialAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'arrive_date',
                    'amount')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'type',
                    'slug',
                    'description')

@admin.register(PropertyValue)
class PropertyValueAdmin(admin.ModelAdmin):
    list_display = ('property',
                    'value',
                    'material')

@admin.register(EquipmentExpendableMaterial)
class PropertyValueAdmin(admin.ModelAdmin):
    list_display = ('equipment',
                    'material',
                    'amount')
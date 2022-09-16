from django.contrib import admin

from programs.models import *


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('developer',
                    'version')

@admin.register(EquipmentProgram)
class EquipmentProgramAdmin(admin.ModelAdmin):
    list_display = ('program',
                    'equipment')
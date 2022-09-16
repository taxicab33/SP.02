from django.db import models
from django.urls import reverse

from app import settings
from classrooms.models import Classroom
from common_data.models import CommonDataModel, CommonRespUserDataModel
from directions.models import EquipmentStatus, EquipmentDirection

EQUIPMENT_URL_ID_KEY = 'inv_number'


class EquipmentType(CommonDataModel):

    class Meta:
        verbose_name = "Тип оборудования"
        verbose_name_plural = "Тип оборудования"
        ordering = ['name']


class Equipment(CommonRespUserDataModel):
    inventory_number = models.PositiveIntegerField(
        verbose_name='Инвентарный номер оборудования',
        unique=True,
        primary_key=True
    )
    classroom = models.ForeignKey(
        Classroom,
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(class)s_classroom',
        verbose_name='Аудитория расположения'
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name='Цена'
    )
    direction = models.ForeignKey(
        EquipmentDirection,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Направление'
    )
    status = models.ForeignKey(
        EquipmentStatus,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Статус'
    )
    model = models.CharField(
        max_length=255,
        verbose_name='Модель'
    )
    comment = models.TextField(
        verbose_name='Комментарий'
    )
    type = models.ForeignKey(
        EquipmentType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Тип оборудования'
    )
    image = models.ImageField(
        upload_to='images/equipment',
        null=True,
        verbose_name='Изображение',
        blank=True
    )

    def get_absolute_url(self):
        return reverse('equipment', kwargs={'pk': self.pk})

    def get_inventory(self):
        """Узнаём, прошло ли оборудование инвентаризацию"""
        from inventory.models import InventoryedEquipment
        inventories = InventoryedEquipment.objects.filter(equipment=self).\
            select_related('inventory')
        if inventories:
            return inventories
        else:
            return False

    def get_classrooms_history(self):
        """Получаем историю передвижения оборудования по аудиториям"""
        history = EquipmentClassroomHistory.objects.filter(equipment=self)
        if history:
            return history
        else:
            return False

    def get_resp_users_history(self):
        """Получаем историю передачи отвественности за оборудования между пользователями"""
        history = EquipmentRespUserHistory.objects.filter(equipment=self).\
            select_related('resp_user')
        if history:
            return history
        else:
            return False

    def get_programs(self):
        """Получаем список установленного ПО на оборудование"""
        from programs.models import EquipmentProgram
        programs = EquipmentProgram.objects.filter(equipment=self).\
            select_related('program__developer', 'program')
        if programs:
            return programs
        else:
            return False

    def get_network_settings(self):
        """Получаем список всех сетевых настроек оборудования"""
        from network_settings.models import NetworkSettings
        settings = NetworkSettings.objects.filter(equipment=self)
        if settings:
            return settings
        else:
            return False

    def get_expendable_materials(self):
        """Получаем все расходные материалы, прикрепленные к оборудованию"""
        from expendable_materials.models import EquipmentExpendableMaterial
        materials = EquipmentExpendableMaterial.objects.filter(equipment=self).select_related('material')
        if materials:
            return materials
        else:
            return False

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"
        ordering = ['inventory_number']

    def __str__(self):
        return f"{self.name} {self.model}"


class BaseEquipmentHistoryDataModel(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name='Оборудование')
    datetime = models.DateTimeField(verbose_name='Дата и время')

    class Meta:
        ordering = ['-datetime']
        abstract = True


class EquipmentClassroomHistory(BaseEquipmentHistoryDataModel):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, verbose_name='Аудитория')

    def __str__(self):
        return f"Оборудование {self.equipment} было в аудитории {self.classroom}"

    class Meta:
        verbose_name = 'История аудитории, к которой было прикрепленно оборудование'
        verbose_name_plural = 'История аудиторий, к которым было прикрепленно оборудование'


class EquipmentRespUserHistory(BaseEquipmentHistoryDataModel):
    resp_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Ответственный')

    def __str__(self):
        return f"Отвественным за {self.equipment} был {self.resp_user}"

    class Meta:
        verbose_name = 'История пользователя, к которому было прикрепленно оборудование'
        verbose_name_plural = 'История пользователей, к которым было прикрепленно оборудование'

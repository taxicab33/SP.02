from common_data.models import CommonDataModel
from django.db import models
from equipment.models import Equipment


class Inventory(CommonDataModel):
    start_date = models.DateField(verbose_name='Дата начала')
    end_date = models.DateField(verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'Инвентаризация'
        verbose_name_plural = 'Инвентаризации'
        ordering = ['-start_date']


class InventoryedEquipment(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.SET_NULL, null=True, verbose_name='Инвентаризация')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name='Оборудование')
    comment = models.TextField(verbose_name="Комментарий")
    inventory_time = models.DateTimeField(auto_now_add=True, verbose_name='Время инветоризации')

    class Meta:
        verbose_name = 'Проинвентаризованное оборудование'
        verbose_name_plural = 'Проинвентаризованное оборудование'
        ordering = ['inventory']



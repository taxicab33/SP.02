from django.db import models

from common_data.models import CommonDataModel
from equipment.models import Equipment


class NetworkSettings(CommonDataModel):
    ip_address = models.GenericIPAddressField(unique=True, verbose_name='IP-адрес')
    mask = models.GenericIPAddressField(verbose_name='Маска подсети')
    main_gate = models.GenericIPAddressField(verbose_name='Главный шлюз')
    dns = models.GenericIPAddressField(verbose_name='DNS-сервера')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name='Оборудование')
    active = models.BooleanField(default=False, verbose_name='Текущая настройка')

    class Meta:
        verbose_name = 'Сетевая настройка оборудования'
        verbose_name_plural = 'Сетевые настройки оборудования'
        ordering = ['-active', 'equipment']

    def save(self, *args, **kwargs):
        if self.active:
            NetworkSettings.objects.filter(active=True).update(active=False)
        super().save(*args, **kwargs)
from common_data.models import CommonDataModel


class EquipmentDirection(CommonDataModel):
    pass

    class Meta:
        verbose_name = "Направления обородувания"
        verbose_name_plural = "Направлении оборудования"
        ordering = ['name']

class EquipmentStatus(CommonDataModel):
    class Meta:
        verbose_name = "Статус оборудования"
        verbose_name_plural = "Статусы оборудования"
        ordering = ['name']


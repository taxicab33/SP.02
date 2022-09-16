from common_data.models import *
from equipment.models import Equipment
from pytils.translit import slugify


class ExpendableMaterialType(CommonDataModel):
    pass

    class Meta:
        verbose_name = 'Тип расходного материала'
        verbose_name_plural = 'Типы расходных материалов'


class ExpendableMaterial(CommonRespUserDataModel):
    description = models.TextField(verbose_name='Описание')
    arrive_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата поступления')
    image = models.ImageField(upload_to='images/materials/',verbose_name='Изображение')
    amount = models.PositiveIntegerField(default=1, verbose_name='Количество')
    type = models.ForeignKey(ExpendableMaterialType, on_delete=models.SET_NULL, null=True)

    def get_properties_and_values(self):
        """Возвращает список характеристи и их значений расходного материала"""
        return PropertyValue.objects.filter(material=self).select_related('property')

    class Meta:
        verbose_name = 'Расходный материал'
        verbose_name_plural = 'Расходный материал'


class EquipmentExpendableMaterial(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name='Оборудование')
    material = models.ForeignKey(ExpendableMaterial, on_delete=models.CASCADE, verbose_name='Расходный материал')
    amount = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"Прикрепленный расходный материал {self.material} к оборудованию {self.equipment}"

    class Meta:
        verbose_name = 'Расходный материала оборудования'
        verbose_name_plural = 'Расходные материалы оборудования'
        ordering = ['equipment']

class Property(CommonDataModel):
    type = models.ForeignKey(ExpendableMaterialType, on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=255, blank=True, null=False, unique=True, verbose_name='Имя для фильтрации')
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.type.name} {self.name}"

    class Meta:
        verbose_name = 'Характеристика расходного материала'
        verbose_name_plural = 'Характеристики расходных материалов'
        ordering = ['type']


class PropertyValue(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='Характеристика')
    value = models.CharField(max_length=255, verbose_name='Значение')
    material = models.ForeignKey(ExpendableMaterial, on_delete=models.CASCADE, verbose_name='Расходный материал')

    class Meta:
        verbose_name = 'Значение характеристики расходного материала'
        verbose_name_plural = 'Значения характеристик расходных материалов'
        ordering = ['material']


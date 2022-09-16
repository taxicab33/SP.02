from django.db import models

from common_data.models import CommonDataModel
from developers.models import Developer
from equipment.models import Equipment


class Program(CommonDataModel):
    developer = models.ForeignKey(Developer, on_delete=models.SET_NULL, null=True,
                                    verbose_name='Разработчик')
    version = models.CharField(max_length=255, verbose_name='Версия ПО')

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'


class EquipmentProgram(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, verbose_name='Программное обеспечение')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, verbose_name='Оборудование')

    def __str__(self):
        return f"Программное обеспечение {self.program} для оборудования {self.equipment}"

    class Meta:
        verbose_name = 'Программное обеспечение оборудования'
        verbose_name_plural = 'Программные обеспечения оборудования'
        ordering = ['equipment']
from django.db import models

from common_data.models import CommonRespUserDataModel


class Classroom(CommonRespUserDataModel):
    short_name = models.CharField(unique=True, max_length=255, verbose_name='Сокращённое название')

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = "Аудитория"
        verbose_name_plural = "Аудитории"
        ordering = ['short_name']


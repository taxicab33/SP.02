from django.db import models
from app import settings


class CommonDataModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Именование')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='%(class)s_creator',
        null=True, verbose_name='Создатель записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано в')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено в')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class CommonRespUserDataModel(CommonDataModel):
    resp_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(class)s_resp_user',
        verbose_name='Отвественный пользователь'
    )
    temp_resp_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='%(class)s_temp_resp_user',
        verbose_name='Временно отвественный пользователь'
    )

    class Meta:
        abstract = True




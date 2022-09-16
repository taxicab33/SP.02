from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

from common_data.logger import db_logger
from equipment.models import *


@receiver(pre_save, sender=Equipment)
def create_equipment_history(sender,  **kwargs):
    """
    Сохраняем историю о передвежении оборудования между аудиториями
    и об передачи отвественности между пользователями.
    """
    instance = kwargs.pop('instance', None)
    created = kwargs.pop('created', False)
    if not created and instance:
        try:
            old_instance = Equipment.objects.get(pk=instance.pk)
            if instance.classroom != old_instance.classroom:
                # если меняется аудитория расположения
                EquipmentClassroomHistory.objects.get_or_create(
                    equipment=old_instance,
                    classroom=old_instance.classroom,
                    datetime=timezone.now())
            if instance.resp_user.pk != old_instance.resp_user.pk:
                # если меняется ответственный пользователь
                EquipmentRespUserHistory.objects.get_or_create(
                    equipment=old_instance,
                    resp_user=old_instance.resp_user,
                    datetime=timezone.now())
        except Equipment.DoesNotExist as e:
            db_logger.exception(e)
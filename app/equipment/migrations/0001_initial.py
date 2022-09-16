# Generated by Django 4.1.1 on 2022-09-16 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classrooms', '0001_initial'),
        ('directions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('name', models.CharField(max_length=255, verbose_name='Именование')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено в')),
                ('inventory_number', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Инвентарный номер оборудования')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/equipment', verbose_name='Изображение')),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_classroom', to='classrooms.classroom', verbose_name='Аудитория расположения')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель записи')),
                ('direction', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directions.equipmentdirection', verbose_name='Направление')),
                ('resp_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_resp_user', to=settings.AUTH_USER_MODEL, verbose_name='Отвественный пользователь')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directions.equipmentstatus', verbose_name='Статус')),
                ('temp_resp_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_temp_resp_user', to=settings.AUTH_USER_MODEL, verbose_name='Временно отвественный пользователь')),
            ],
            options={
                'verbose_name': 'Оборудование',
                'verbose_name_plural': 'Оборудование',
                'ordering': ['inventory_number'],
            },
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Именование')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено в')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель записи')),
            ],
            options={
                'verbose_name': 'Тип оборудования',
                'verbose_name_plural': 'Тип оборудования',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EquipmentRespUserHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата и время')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment', verbose_name='Оборудование')),
                ('resp_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Ответственный')),
            ],
            options={
                'verbose_name': 'История пользователя, к которому было прикрепленно оборудование',
                'verbose_name_plural': 'История пользователей, к которым было прикрепленно оборудование',
            },
        ),
        migrations.CreateModel(
            name='EquipmentClassroomHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата и время')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classrooms.classroom', verbose_name='Аудитория')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment', verbose_name='Оборудование')),
            ],
            options={
                'verbose_name': 'История аудитории, к которой было прикрепленно оборудование',
                'verbose_name_plural': 'История аудиторий, к которым было прикрепленно оборудование',
            },
        ),
        migrations.AddField(
            model_name='equipment',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipment.equipmenttype', verbose_name='Тип оборудования'),
        ),
    ]
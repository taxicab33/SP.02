# Generated by Django 4.1.1 on 2022-09-16 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Именование')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено в')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель записи')),
            ],
            options={
                'verbose_name': 'Инвентаризация',
                'verbose_name_plural': 'Инвентаризации',
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='InventoryedEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('inventory_time', models.DateTimeField(auto_now_add=True, verbose_name='Время инветоризации')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment', verbose_name='Оборудование')),
                ('inventory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.inventory', verbose_name='Инвентаризация')),
            ],
            options={
                'verbose_name': 'Проинвентаризованное оборудование',
                'verbose_name_plural': 'Проинвентаризованное оборудование',
                'ordering': ['inventory'],
            },
        ),
    ]

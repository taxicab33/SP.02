# Generated by Django 4.1.1 on 2022-09-16 12:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('developers', '0001_initial'),
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Именование')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано в')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено в')),
                ('version', models.CharField(max_length=255, verbose_name='Версия ПО')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_creator', to=settings.AUTH_USER_MODEL, verbose_name='Создатель записи')),
                ('developer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='developers.developer', verbose_name='Разработчик')),
            ],
            options={
                'verbose_name': 'Программа',
                'verbose_name_plural': 'Программы',
            },
        ),
        migrations.CreateModel(
            name='EquipmentProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment', verbose_name='Оборудование')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programs.program', verbose_name='Программное обеспечение')),
            ],
            options={
                'verbose_name': 'Программное обеспечение оборудования',
                'verbose_name_plural': 'Программные обеспечения оборудования',
                'ordering': ['equipment'],
            },
        ),
    ]

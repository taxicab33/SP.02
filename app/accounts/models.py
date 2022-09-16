from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    surname = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Отчество')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')
    image = models.ImageField(upload_to='images/users', blank=True, null=True, verbose_name='Изображение профиля')
    phone_number = models.CharField(max_length=11, null=True, blank=True, verbose_name="Номер телефона")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Адрес")
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False, verbose_name='Доступ администратора')
    is_staff = models.BooleanField(default=False, verbose_name="Сотрудник организации")
    role = models.CharField(max_length=255, null=True, default='Сотрудник', verbose_name='Права доступа')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        ''' Вовзращает ФИО с пробелами '''
        return f"{self.surname} {self.first_name} {self.last_name}"
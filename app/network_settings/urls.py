from django.urls import path
from equipment.views import *
from network_settings.views import *


urlpatterns = [
    path('setting/create/<int:equip_pk>', SettingCreateView.as_view(), name='add_setting'),
    path('setting/edit/<int:pk>', SettingEditView.as_view(), name='edit_setting'),
    path('setting/delete/<int:pk>', SettingDeleteView.as_view(), name='delete_setting'),
]

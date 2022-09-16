from django.urls import path
from equipment.views import *

urlpatterns = [
    path('', EquipmentListView.as_view(), name='equipment'),
    path('equipment/', EquipmentListView.as_view(), name='equipment'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment_detail'),
    path('equipment/create/', EquipmentCreateView.as_view(), name='create_equipment'),
    path('equipment/edit/<int:pk>', EquipmentEditView.as_view(), name='edit_equipment'),
    path('equipment/delete/<int:pk>', EquipmentDeleteView.as_view(), name='delete_equipment'),
]

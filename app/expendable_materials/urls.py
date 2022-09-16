from django.urls import path
from equipment.views import *
from expendable_materials.views import *

urlpatterns = [
    path('expendable_materials/', ExpendableMaterialListView.as_view(), name='expendable_materials'),
    path('expendable_materials/create', ExpendableMaterialCreateView.as_view(), name='create_material'),
    path('expendable_materials/<int:pk>/', ExpendableMaterialDetailView.as_view(), name='material_detail'),
    path('expendable_materials/<int:pk>/edit', ExpendableMaterialEditView.as_view(), name='edit_material'),
    path('expendable_materials/<int:pk>/delete', ExpendableMaterialDeleteView.as_view(), name='delete_material'),
    path('expendable_materials/attach_material_to_equipment/<int:pk>', EquipmentExpendableMaterialAtachView.as_view(),
         name='attach_material'),
    path('equipment_expendable_materials/edit/<int:pk>', EquipmentExpendableMaterialUpdateView.as_view(),
         name='edit_attached_material'),
    path('equipment_expendable_materials/delete/<int:pk>', EquipmentExpendableMaterialDeleteView.as_view(),
         name='delete_attached_material'),
]

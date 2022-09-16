from django.urls import path
from equipment.views import *
from programs.views import *

urlpatterns = [
    path('program/', ProgramListView.as_view(), name='programs'),
    path('program/create', ProgramCreateView.as_view(), name='create_program'),
    path('program/<int:pk>/', ProgramDetailView.as_view(), name='program_detail'),
    path('program/<int:pk>/edit', ProgramUpdateView.as_view(), name='edit_program'),
    path('program/<int:pk>/delete', ProgramDeleteView.as_view(), name='delete_program'),
    path('program/equipment_program/create/<int:pk>', EquipmentProgramCreateView.as_view(),
         name='attach_program'),
    path('program/equipment_program/edit/<int:pk>', EquipmentProgramUpdateView.as_view(),
         name='edit_attached_program'),
    path('program/equipment_program/delete/<int:pk>', EquipmentProgramDeleteView.as_view(),
         name='delete_attached_program'),
]

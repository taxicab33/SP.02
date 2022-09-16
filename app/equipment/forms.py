from django import forms

from common_data.forms import CommonRespUserForm, CommonDataModelForm
from equipment.models import Equipment


class EquipmentModelForm(CommonRespUserForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = "Категория не выбрана"
        self.fields['direction'].empty_label = "Направление не выбрано"
        self.fields['status'].empty_label = "Статус не указан"
        self.fields['classroom'].empty_label = "Аудитория не выбрана"

    class Meta(CommonDataModelForm.Meta):
        model = Equipment
        fields = '__all__'
        widgets = {
            'inventory_number': forms.NumberInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
            'price': forms.NumberInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
            'model': forms.TextInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
            'comment': forms.Textarea(attrs={'class': 'input-group inputs mb-2 mt-2'}),
        }
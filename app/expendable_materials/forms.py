from expendable_materials.models import *
from common_data.forms import CommonRespUserForm, CommonDataModelForm
from django import forms


class ExpendableModelForm(CommonRespUserForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = "Категория не выбрана"

    class Meta(CommonDataModelForm.Meta):
        model = ExpendableMaterial
        fields = '__all__'
        widgets = {
            'arrive_date': forms.NumberInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
            'amount': forms.NumberInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
            'description': forms.Textarea(attrs={'class': 'input-group inputs mb-2 mt-2'}),
        }


class EquipmentExpendableMaterialModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['material'].empty_label = "Выбрать"

    class Meta(CommonDataModelForm.Meta):
        model = EquipmentExpendableMaterial
        exclude = ('equipment', )
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
        }
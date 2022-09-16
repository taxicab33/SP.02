from expendable_materials.models import ExpendableMaterial
from common_data.forms import CommonRespUserForm, CommonDataModelForm
from django import forms
from programs.models import *

class ProgramForm(CommonDataModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['developer'].empty_label = "Разработчик не выбран"

    class Meta(CommonDataModelForm.Meta):
        model = Program
        fields = '__all__'
        widgets = {
            'version': forms.TextInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
        }


class EquipmentProgramForm(CommonDataModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['program'].empty_label = "Выберите"

    class Meta(CommonDataModelForm.Meta):
        model = EquipmentProgram
        exclude = ('equipment', )
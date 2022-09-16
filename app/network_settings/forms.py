from expendable_materials.models import ExpendableMaterial
from common_data.forms import CommonRespUserForm, CommonDataModelForm
from django import forms
from network_settings.models import *

class NetworkSettingsForm(CommonDataModelForm):


    class Meta(CommonDataModelForm.Meta):
        model = NetworkSettings
        exclude = ('equipment', 'creator')
        widgets = {
            'ip_address': forms.TextInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
            'mask': forms.TextInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
            'main_gate': forms.TextInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
            'dns': forms.TextInput(attrs={'class': 'input-group inputs mb-2 mt-2'}),
        }
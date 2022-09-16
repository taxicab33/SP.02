from django import forms

from .models import *


class CommonDataModelForm(forms.ModelForm):

    class Meta:
        model = CommonDataModel
        exclude = ('creator', )


class CommonRespUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resp_user'].empty_label = "Отвественный пользователь не выбран"
        self.fields['temp_resp_user'].empty_label = "Временно отвественный пользователь не выбран"

    class Meta:
        fields = '__all__'
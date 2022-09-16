from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import *
from network_settings.models import *
from network_settings.forms import *
from equipment.models import Equipment


class SettingCreateView(CreateView):
    model = NetworkSettings
    form_class = NetworkSettingsForm
    template_name = 'common_data/form.html'
    success_url = reverse_lazy('equipment')

    def form_valid(self, form_class):
        equipment = Equipment.objects.get(pk=self.kwargs['equip_pk'])
        form_class.instance.creator = self.request.user
        form_class.instance.equipment = equipment
        return super().form_valid(form_class)

class SettingEditView(UpdateView):
    model = NetworkSettings
    template_name = 'common_data/form.html'
    form_class = NetworkSettingsForm
    success_url = reverse_lazy('equipment')


class SettingDeleteView(DeleteView):
    model = NetworkSettings
    template_name = 'common_data/confirm_delete.html'
    success_url = reverse_lazy('equipment')
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from equipment.forms import EquipmentModelForm
from equipment.models import Equipment
from equipment.utils import EquipmentMixin


class EquipmentListView(ListView, LoginRequiredMixin):
    model = Equipment
    template_name = 'equipment/main.html'
    context_object_name = 'equipment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Оборудование'
        return context


class EquipmentDetailView(DetailView, EquipmentMixin):
    model = Equipment
    template_name = 'equipment/detail_page.html'
    context_object_name = 'equipment_object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['equipment_object']
        return self.get_equipment_extra_context_data(context)


class EquipmentCreateView(CreateView):
    form_class = EquipmentModelForm
    template_name = 'equipment/form.html'
    success_url = reverse_lazy('equipment')

    def form_valid(self, form_class):
        form_class.instance.user = self.request.user
        return super().form_valid(form_class)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Добавление оборудования"
        return context


class EquipmentEditView(LoginRequiredMixin, UpdateView):
    model = Equipment
    form_class = EquipmentModelForm
    template_name = 'equipment/form.html'
    success_url = reverse_lazy('equipment')

    def form_valid(self, form_class):
        form_class.instance.creator = self.request.user
        return super().form_valid(form_class)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Редактирование оборудования"
        return context


class EquipmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Equipment
    success_url = reverse_lazy('equipment')
    template_name = 'common_data/confirm_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Удаление объекта из системы"
        return context



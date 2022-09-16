from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from django.urls import reverse_lazy
from expendable_materials.forms import *
from expendable_materials.models import ExpendableMaterial


class ExpendableMaterialListView(ListView, LoginRequiredMixin):
    model = ExpendableMaterial
    template_name = 'expendable_materials/main.html'
    context_object_name = 'materials'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Расходные материалы"
        return context


class ExpendableMaterialDetailView(DetailView):
    model = ExpendableMaterial
    template_name = 'expendable_materials/detail_page.html'
    context_object_name = 'material_object'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['material_object']
        return context

class ExpendableMaterialEditView(UpdateView):
    model = ExpendableMaterial
    form_class = ExpendableModelForm
    template_name = 'common_data/form.html'
    success_url = reverse_lazy('expendable_materials')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Редактирование материала"
        return context


class ExpendableMaterialCreateView(CreateView):
    model = ExpendableMaterial
    form_class = ExpendableModelForm
    template_name = 'common_data/form.html'
    success_url = reverse_lazy('expendable_materials')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Добавление материала"
        return context

class ExpendableMaterialDeleteView(LoginRequiredMixin, DeleteView):
    model = ExpendableMaterial
    success_url = reverse_lazy('expendable_materials')
    template_name = 'common_data/confirm_delete.html'


class EquipmentExpendableMaterialAtachView(CreateView):
    model = EquipmentExpendableMaterial
    form_class = EquipmentExpendableMaterialModelForm
    template_name = 'common_data/form.html'
    success_url = reverse_lazy('equipment')

    def form_valid(self, form_class):
        equipment = Equipment.objects.get(pk=self.kwargs['pk'])
        form_class.instance.equipment = equipment
        return super().form_valid(form_class)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Прикрепление материала к оборудованию"
        return context


class EquipmentExpendableMaterialUpdateView(UpdateView):
    model = EquipmentExpendableMaterial
    form_class = EquipmentExpendableMaterialModelForm
    template_name = 'common_data/form.html'
    success_url = reverse_lazy('equipment')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Изменение кол-ва прикрепленного материала к оборудованию"
        return context

class EquipmentExpendableMaterialDeleteView(DeleteView):
    model = EquipmentExpendableMaterial
    form_class = EquipmentExpendableMaterialModelForm
    template_name = 'common_data/confirm_delete.html'
    success_url = reverse_lazy('equipment')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f"Отпреление материала от оборудования"
        return context
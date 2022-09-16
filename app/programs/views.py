from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import *
from programs.models import *
from programs.forms import *

class ProgramListView(ListView):
    model = Program
    template_name = 'programs/main.html'
    context_object_name = 'programs'

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'programs/main.html'
    context_object_name = 'programs'


class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'common_data/form.html'
    success_url = reverse_lazy('programs')


class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'common_data/form.html'
    success_url = reverse_lazy('programs')


class ProgramDeleteView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'common_data/confirm_delete.html'
    success_url = reverse_lazy('programs')

class EquipmentProgramCreateView(CreateView):
    model = EquipmentProgram
    form_class = EquipmentProgramForm
    template_name = 'common_data/form.html'
    success_url = reverse_lazy('equipment')

    def form_valid(self, form_class):
        equipment = Equipment.objects.get(pk=self.kwargs['pk'])
        form_class.instance.equipment = equipment
        return super().form_valid(form_class)

class EquipmentProgramUpdateView(UpdateView):
    model = EquipmentProgram
    form_class = EquipmentProgramForm
    template_name = 'common_data/form.html'
    success_url = reverse_lazy('equipment')


class EquipmentProgramDeleteView(DeleteView):
    model = EquipmentProgram
    template_name = 'common_data/confirm_delete.html'
    success_url = reverse_lazy('equipment')
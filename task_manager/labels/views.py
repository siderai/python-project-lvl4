from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.labels.models import Label


class Labels(LoginRequiredMixin, FormView):
    def get(self, request):
        labels = Label.objects.all()
        return render(request, 'labels.html', {'labels': labels})


class LabelCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'label-create.html'
    success_message = 'Метка успешно создана'
    success_url = '/labels/'


class LabelUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = 'label-update.html'
    success_message = 'Метка успешно изменена'
    success_url = '/labels/'


class LabelDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    fields = ['name']
    template_name = 'label-delete.html'
    success_message = 'Метка успешно удалена'
    success_url = '/labels/'

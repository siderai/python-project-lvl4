from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Status


class Statuses(LoginRequiredMixin, FormView):
    def get(self, request):
        statuses = Status.objects.all()
        return render(request, 'statuses.html', {'statuses': statuses})


class StatusCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'status-create.html'
    success_message = 'Статус успешно создан'
    success_url = '/statuses/'


class StatusUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'status-update.html'
    success_message = 'Статус успешно изменён'
    success_url = '/statuses/'


class StatusDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    fields = ['name']
    template_name = 'status-delete.html'
    success_message = 'Статус успешно удалён'
    success_url = '/statuses/'

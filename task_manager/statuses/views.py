from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.statuses.models import Status
from task_manager.statuses.utils import StatusMixin


class Statuses(LoginRequiredMixin, FormView):
    def get(self, request):
        statuses = Status.objects.all()
        return render(request, "statuses.html", {"statuses": statuses})


class StatusCreate(LoginRequiredMixin,
                   SuccessMessageMixin,
                   StatusMixin,
                   CreateView):
    template_name = "status-create.html"
    success_message = "Статус успешно создан"


class StatusUpdate(LoginRequiredMixin,
                   SuccessMessageMixin,
                   StatusMixin,
                   UpdateView):
    template_name = "status-update.html"
    success_message = "Статус успешно изменён"


class StatusDelete(LoginRequiredMixin,
                   SuccessMessageMixin,
                   StatusMixin,
                   DeleteView):
    template_name = "status-delete.html"
    success_message = "Статус успешно удалён"

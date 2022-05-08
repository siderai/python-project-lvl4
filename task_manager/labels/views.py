from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.labels.models import Label
from task_manager.labels.utils import LabelMixin


class Labels(LoginRequiredMixin, FormView):
    def get(self, request):
        labels = Label.objects.all()
        return render(request, "labels.html", {"labels": labels})


class LabelCreate(LoginRequiredMixin, SuccessMessageMixin, LabelMixin, CreateView):
    template_name = "label-create.html"
    success_message = "Метка успешно создана"


class LabelUpdate(LoginRequiredMixin, SuccessMessageMixin, LabelMixin, UpdateView):
    template_name = "label-update.html"
    success_message = "Метка успешно изменена"


class LabelDelete(LoginRequiredMixin, SuccessMessageMixin, LabelMixin, DeleteView):
    template_name = "label-delete.html"
    success_message = "Метка успешно удалена"

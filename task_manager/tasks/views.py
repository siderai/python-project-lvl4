from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class Tasks(LoginRequiredMixin, FormView):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'tasks-list.html', {'tasks': tasks})


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    fields = ['name']
    template_name = 'task-create.html'
    success_message = 'Задача успешно создана'
    success_url = '/tasks/'


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    fields = ['name']
    template_name = 'task-update.html'
    success_message = 'Задача успешно изменена'
    success_url = '/tasks/'


class TaskDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    fields = ['name']
    template_name = 'task-delete.html'
    success_message = 'Задача успешно удалена'
    success_url = '/tasks/'
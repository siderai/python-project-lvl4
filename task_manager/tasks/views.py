from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.tasks.utils import TaskMixin
from task_manager.tasks.models import Task


class Tasks(LoginRequiredMixin, FormView):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'tasks-list.html', {'tasks': tasks})


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin,
                 TaskMixin, CreateView):
    template_name = 'task-create.html'
    success_message = 'Задача успешно создана'


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin,
                 TaskMixin, UpdateView):
    template_name = 'task-update.html'
    success_message = 'Задача успешно изменена'


class TaskDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    fields = ['name']
    template_name = 'task-delete.html'
    success_message = 'Задача успешно удалена'
    success_url = '/tasks/'

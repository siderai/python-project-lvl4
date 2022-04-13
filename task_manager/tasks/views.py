from django.shortcuts import render
from django.views import View
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class Tasks(LoginRequiredMixin, FormView):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'tasks-list.html', {'tasks': tasks})


class TaskMixin(View):  # if ok remove dupli in other views
    model = Task
    fields = ['name', 'description', 'author', 'status', 'executor', 'label']
    success_url = '/tasks/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["labels"] = Label.objects.all()
        context["statuses"] = Status.objects.all()
        context["users"] = User.objects.all()
        # context["user"] = self.request.user
        # context['task'] = Task.objects.filter(name=Task.name)
        return context


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
    fields = ['name', 'description', 'status', 'executor', 'label']
    template_name = 'task-delete.html'
    success_message = 'Задача успешно удалена'
    success_url = '/tasks/'

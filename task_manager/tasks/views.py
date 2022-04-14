from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.tasks.utils import TaskMixin
from task_manager.tasks.models import Task


class TaskView(View):
    def get(self, request, pk):
        task_selected = (
            Task.objects.select_related("executor", "status", "author")
            .prefetch_related("labels")
            .get(pk=pk)
        )
        return render(request, "task-page.html", {"task": task_selected})


class Tasks(LoginRequiredMixin, FormView):
    def get(self, request):
        tasks = Task.objects.select_related("executor", "status", "author").all()
        return render(request, "task-list.html", {"tasks": tasks})


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, TaskMixin, CreateView):
    template_name = "task-create.html"
    success_message = "Задача успешно создана"


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, TaskMixin, UpdateView):
    template_name = "task-update.html"
    success_message = "Задача успешно изменена"


class TaskDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    fields = ["name"]
    template_name = "task-delete.html"
    success_message = "Задача успешно удалена"
    success_url = "/tasks/"

    def get(self, request, pk):
        self.object = self.get_object()

        if self.object.author == request.user.pk:
            render(request, "task-delete.html")
        else:
            messages.error(request, "Задачу может удалить только её автор")
            return redirect("/tasks/")

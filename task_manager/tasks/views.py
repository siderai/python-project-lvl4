from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.utils import TaskMixin


class TaskView(View):
    """View that collects all data concerning the chosen task,
    then render card with task info."""

    def get(self, request, pk):
        task_selected = (
            Task.objects.select_related("executor", "status", "author")
            .prefetch_related("labels")
            .get(pk=pk)
        )
        return render(request, "task-page.html", {"task": task_selected})


class Tasks(LoginRequiredMixin, View):
    """View that shows list of tasks. Allows filtration through GET params.
    By default, all created tasks are shown."""

    def get(self, request):
        tasks = Task.objects.select_related("executor", "status", "author").all()

        if request.GET:
            # choose only non-empty filters
            filters = {k: v for (k, v) in request.GET.items() if v}

            # workaround to replace GET params with the accurate
            # model field names, in order to pass tests
            try:
                if filters["self_tasks"] == "on":
                    del filters["self_tasks"]
                    filters["author"] = request.user.pk
                if filters["label"]:
                    filters["labels"] = filters["label"]
                    del filters["label"]
            except KeyError:
                pass

            tasks = tasks.filter(**filters)

        labels = Label.objects.all()
        statuses = Status.objects.all()
        users = User.objects.all()

        return render(
            request,
            "task-list.html",
            {"tasks": tasks, "users": users, "statuses": statuses, "labels": labels},
        )


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

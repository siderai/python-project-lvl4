from django.views import View
from django.urls import reverse
from django.contrib.auth.models import User

from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class TaskMixin(View):
    model = Task
    fields = ["name", "description", "author", "status", "executor", "labels"]
    success_url = '/tasks/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["labels"] = Label.objects.all()
        context["statuses"] = Status.objects.all()
        context["users"] = User.objects.all()
        context["tasks"] = Task.objects.all()

        return context

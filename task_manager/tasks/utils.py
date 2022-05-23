from django.views import View
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


class TaskFilter:
    """Filtration through GET params. Full list of tasks
    is shown by default."""

    def _filter(self, request, tasks):
        if request.GET:
            # choose only non-empty filters
            filters = {k: v for (k, v) in request.GET.items() if v}
            # workaround to replace GET params with the accurate
            # model field names, in order to pass tests

            if "self_tasks" in filters:
                if filters["self_tasks"] == "on":
                    del filters["self_tasks"]
                    filters["author"] = request.user.pk

            if "label" in filters:
                filters["labels"] = filters["label"]
                del filters["label"]

            tasks = tasks.filter(**filters)
        return tasks

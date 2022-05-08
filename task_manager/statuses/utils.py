from django.views import View

from task_manager.statuses.models import Status


class StatusMixin(View):
    model = Status
    fields = ["name"]
    success_url = '/statuses/'
    redirect_field_name = None

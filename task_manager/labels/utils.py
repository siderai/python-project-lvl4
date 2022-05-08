from django.views import View

from task_manager.labels.models import Label


class LabelMixin(View):
    model = Label
    fields = ["name"]
    success_url = '/labels/'
    redirect_field_name = None

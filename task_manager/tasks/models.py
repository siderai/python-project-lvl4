from django.db import models
from django.contrib.auth.models import User

from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=150)
    author = models.ForeignKey(
                        User,
                        on_delete=models.PROTECT,
                        related_name='author'
                        )
    executant = models.ForeignKey(
                        User,
                        on_delete=models.PROTECT,
                        related_name='executant'
                        )
    status = models.ForeignKey(
                        Status,
                        on_delete=models.PROTECT
                        )
    label = models.ManyToManyField(
                    Label,
                    on_delete=models.PROTECT
                    )
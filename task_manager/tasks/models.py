from django.db import models
from django.contrib.auth.models import User

from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='author'
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executor',
        blank=True,
        default=None
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        blank=True,
        default=None
    )
    label = models.ManyToManyField(
        Label,
        blank=True,
        default=None
    )

from rest_framework import serializers

from django.contrib.auth.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("first_name", "last_name", "username", "password")
        model = User


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "created_at",
        )
        model = Label


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "created_at",
        )
        model = Status


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "name",
            "description",
            "created_at",
            "author",
            "executor",
            "status",
            "labels",
        )
        model = Task

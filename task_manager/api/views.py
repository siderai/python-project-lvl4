from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django.contrib.auth.models import User

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from .permissions import IsAuthorOrReadOnly, IsCurrentUser
from .serializers import (
    UserSerializer,
    LabelSerializer,
    StatusSerializer,
    TaskSerializer,
)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsCurrentUser or IsAdminUser,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LabelList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Label.objects.all()
    serializer_class = LabelSerializer


class StatusList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TaskList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly or IsAdminUser,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

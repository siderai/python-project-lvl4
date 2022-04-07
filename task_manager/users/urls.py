from django.contrib import admin
from django.urls import path, include

from task_manager.users import views


urlpatterns = [
    path('', views.Users.as_view()),
    path('create/', views.CreateUser.as_view()),
    path('<int:pk>/update/', views.UpdateUser.as_view()),
    path('<int:pk>/delete/', views.DeleteUser.as_view()),
]

from django.urls import path

from task_manager.tasks import views


urlpatterns = [
    path('', views.Tasks.as_view()),
    path('create/', views.TaskCreate.as_view()),
    path('<int:pk>/', views.TaskView.as_view()),
    path('<int:pk>/update/', views.TaskUpdate.as_view()),
    path('<int:pk>/delete/', views.TaskDelete.as_view()),
]

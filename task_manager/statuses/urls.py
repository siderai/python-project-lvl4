from django.urls import path

from task_manager.statuses import views


urlpatterns = [
    path('', views.Statuses.as_view()),
    path('create/', views.StatusCreate.as_view()),
    path('<int:pk>/update/', views.StatusUpdate.as_view()),
    path('<int:pk>/delete/', views.StatusDelete.as_view()),
]
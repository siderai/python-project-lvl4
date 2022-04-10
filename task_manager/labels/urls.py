from django.urls import path

from task_manager.labels import views


urlpatterns = [
    path('', views.Labels.as_view()),
    path('create/', views.LabelCreate.as_view()),
    path('<int:pk>/update/', views.LabelUpdate.as_view()),
    path('<int:pk>/delete/', views.LabelDelete.as_view()),
]

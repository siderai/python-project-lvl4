from django.urls import path

from task_manager.statuses import views


urlpatterns = [
    path('', views.Statuses.as_view(), name="statuses"),
    path('create/', views.StatusCreate.as_view(), name="statuses_create"),
    path('<int:pk>/update/', views.StatusUpdate.as_view(), name="statuses_update"),
    path('<int:pk>/delete/', views.StatusDelete.as_view(), name="statuses_delete"),
]
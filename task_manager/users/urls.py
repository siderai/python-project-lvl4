from django.urls import path

from task_manager.users import views


urlpatterns = [
    path("", views.Users.as_view(), name="users"),
    path("create/", views.CreateUser.as_view(), name="users_create"),
    path("<int:pk>/update/", views.UpdateUser.as_view(), name="users_update"),
    path("<int:pk>/delete/", views.DeleteUser.as_view(), name="users_delete"),
]

from django.urls import path

from task_manager.api import views


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
    path("labels/", views.LabelList.as_view()),
    path("labels/<int:pk>/", views.LabelDetail.as_view()),
    path("statuses/", views.StatusList.as_view()),
    path("statuses/<int:pk>/", views.StatusDetail.as_view()),
    path("tasks/", views.TaskList.as_view()),
    path("tasks/<int:pk>/", views.TaskDetail.as_view()),
]

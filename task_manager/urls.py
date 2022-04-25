from django.contrib import admin
from django.urls import path, include

from task_manager import views, settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.HomePageView.as_view(), name='home'),
    path("login/", views.Login.as_view(), name='login'),
    path("logout/", views.Logout.as_view(), name='logout'),
    path("users/", include("task_manager.users.urls")),
    path("statuses/", include("task_manager.statuses.urls")),
    path("tasks/", include("task_manager.tasks.urls")),
    path("labels/", include("task_manager.labels.urls")),
]

if settings.DEBUG:
    import debug_toolbar # noqa

    urlpatterns = [
        path("__debug__/", include("debug_toolbar.urls")),
    ] + urlpatterns

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from task_manager import views


schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version="v1",
        description="Useful tool for both personal and team projects",
        contact=openapi.Contact(email="sidai@bk.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # templates
    path("admin/", admin.site.urls),
    path("", views.HomePageView.as_view(), name="home"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("users/", include("task_manager.users.urls")),
    path("statuses/", include("task_manager.statuses.urls")),
    path("tasks/", include("task_manager.tasks.urls")),
    path("labels/", include("task_manager.labels.urls")),
    # api
    path("api/v1/", include("task_manager.api.urls")),
    path("api-auth", include("rest_framework.urls")),
    path("api/v1/rest-auth", include("rest_auth.urls")),
    path("api/v1/rest-auth/registration", include("rest_auth.registration.urls")),
    # api docs
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]

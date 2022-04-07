from django.contrib import admin
from django.urls import path, include

from task_manager import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
]

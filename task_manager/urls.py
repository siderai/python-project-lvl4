"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from task_manager import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index.as_view()),
    path('users/', views.Users.as_view()),
    path('users/create/', views.CreateUser.as_view()),
    path('users/<int:pk>/update/', views.UpdateUser.as_view()),
    path('users/<int:pk>/delete/', views.DeleteUser.as_view()),
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    # path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    # path('tasks/', include('task_manager.tasks.urls')),
    # path('labels/', include('task_manager.labels.urls')),
]

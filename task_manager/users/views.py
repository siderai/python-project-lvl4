from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from task_manager.users.forms import NewUserForm, UpdateUserForm


class Users(View):
    def get(self, request):
        User = get_user_model()
        users = User.objects.all()
        return render(request, 'users.html', {'users': users})


class CreateUser(View):
    def get(self, request):
        form = NewUserForm()
        return render(request, 'user-create.html', {'form': form})

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password
                )
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('/login', username=user.username)
        else:
            # error
            return render(request, 'user-create.html', {'form': form})


class UpdateUser(LoginRequiredMixin, SuccessMessageMixin, View):
    redirect_field_name = None

    def get(self, request, pk):
        if pk == request.user.id and request.user.is_authenticated:
            return render(request, 'user-update.html', {'user': request.user})
        elif not request.user.is_authenticated:
            messages.error(request, 'Вы не авторизованы! Пожалуйста, выполните вход.')
            return redirect('/login/')
        else:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return redirect('/users/')


    def post(self, request, pk):
        if pk == request.user.id and request.user.is_authenticated:
            user = User.objects.get(pk=pk)
            form = UpdateUserForm(data=request.POST, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                messages.success(request, 'Пользователь успешно изменён')
                return redirect('/users/')
            else:
                render(request, 'user-update.html', {'user': request.user})
        else:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')


class DeleteUser(LoginRequiredMixin, View):
    redirect_field_name = None

    def get(self, request, pk):
        if pk == request.user.id:
            return render(request, 'user-delete.html', {'user': request.user})
        else:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return redirect('/users/')

    def post(self, request, pk):
        if pk == request.user.id:
            user = User.objects.get(pk=pk)
            if user:
                user.delete()
                messages.success(request, 'Пользователь успешно удалён')
            return redirect('/users/')
        else:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return redirect('/users/')

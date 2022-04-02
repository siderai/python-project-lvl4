from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from task_manager.forms import NewUserForm, LoginForm, UpdateUserForm


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class Users(View):
    def get(self, request):
        User = get_user_model()
        users = User.objects.all()
        return render(request, 'users.html', {'users': users})


class CreateUser(View):
    def get(self, request):
        form = NewUserForm()
        return render(request, 'create-user.html', {'form': form})

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
            return redirect('/login')
        else:
            # error
            return render(request, 'create-user.html', {'form': form})


class UpdateUser(LoginRequiredMixin, View):
    def get(self, request, pk):
        if pk == request.user.id:
            return render(request, 'update-user.html', {'user': request.user})
        else:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')
            return redirect('/users/')

    def post(self, request, pk):
        if pk == request.user.id:
            user = User.objects.get(pk=pk)
            form = UpdateUserForm(data=request.POST, instance=user)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                messages.success(request, 'Пользователь успешно изменён')
                return redirect('/users/')
            else:
                render(request, 'update-user.html', {'user': request.user})
        else:
            messages.error(request, 'У вас нет прав для изменения другого пользователя.')


class DeleteUser(LoginRequiredMixin, View):
    def get(self, request, pk):
        if pk == request.user.id:
            return render(request, 'delete-user.html', {'user': request.user})
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


class Login(SuccessMessageMixin, View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Вы залогинены')
                    return redirect('/')

            messages.error(request, 'Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру.')
            return render(request, 'login.html', {'form': form})


class Logout(View):
    def post(self, request):
        logout(request)
        messages.info(request, 'Вы разлогинены') # blue
        return redirect('/')

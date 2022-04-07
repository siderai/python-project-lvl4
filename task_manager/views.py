from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View

from task_manager.forms import LoginForm


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


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

            messages.error(request, 
                'Пожалуйста, введите правильные имя пользователя и пароль. '\
                'Оба поля могут быть чувствительны к регистру.')
            return render(request, 'login.html', {'form': form})


class Logout(View):
    def post(self, request):
        logout(request)
        messages.info(request, 'Вы разлогинены')
        return redirect('/')

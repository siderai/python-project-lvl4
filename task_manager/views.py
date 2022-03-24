from django.contrib.auth import login, authenticate, get_user_model
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View

from task_manager.forms import NewUserForm


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
            form.save()
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
            # after form will work properly
            # user = authenticate(request, username=username, password=password)
            # login(request, user)
            return HttpResponseRedirect('/')

        # return render(request, 'create-user.html')



            # user = User.objects.create_user(username, email, password)
            # user.save()


class UpdateUser(View):
    def get(request):
        pass
        
    def post(request):
        pass



class DeleteUser(View):
    def get(request):
        pass
        
    def post(request):
        pass






class Login(View):
    def get(request):
        pass

    def post(request):
        pass


class Logout(View):
    pass


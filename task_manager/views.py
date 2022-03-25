from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.decorators import login_required
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

            return redirect('/login/')

        form = NewUserForm()
        return render(request, 'create-user.html', {'form': form})



class UpdateUser(View):
    def get(self, request, pk):
        return render(request, 'update-user.html', {'user': request.user})

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        form = UpdateUserForm(data=request.POST, instance=user)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user.save()
            # flash msg
            return redirect('/users/')


class DeleteUser(View):
    def get(self, request, pk):
        return render(request, 'delete-user.html', {'user': request.user})

    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        if user:
            user.delete()
        # flash msg
        return redirect('/users/')




class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # flash msg
                    return redirect('/')
                else:
                    # flash msg
                    return render(request, 'login.html')
            else:
                # flash msg
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')



class Logout(View):
    def post(self, request):
        pass

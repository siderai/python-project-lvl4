from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View


class Index(View):
    def get(self, request):
        return render(request, 'index.html')


class Users(View):
    def get(self, request):
        # User = get_user_model()
        # users = User.objects.all()
        return render(request, 'users.html')


class CreateUser(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'create-user.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request)
        if form.id_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate((username, password))
            login(request, user)
            return redirect('')
        # else:
        #     form = UserCreationForm()
        # return render(request, 'signup.html', {'form': form})



            # user = User.objects.create_user(username, email, password)
            # user.save()


class Login(View):
    pass


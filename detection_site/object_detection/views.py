from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import  UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def index2(request):
    return render(request, 'object_detection/home.html')


def login1(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
            # аутефикация
        user=authenticate(request,username=username,password=password)
        if user:
            login1(request,user)
            return redirect("http://127.0.0.1:8000/")
        else:
            return render(request, 'object_detection/login.html',{'error': 'Неверные учетные данные'})
    return render(request, 'object_detection/login.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_login'))
    else:
        form = UserRegisterForm()
    return render(request, "object_detection/register.html", {"form": form})


def dashboard(request):
    return render(request, 'object_detection/dashboard.html')



def logout1(request):
    logout(request)
    return redirect(reverse('user_login'))

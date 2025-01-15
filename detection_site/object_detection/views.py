from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required

@login_required
def index2(request):
    return render(request, 'object_detection/home.html')


def login1(request):
    if request.method=='POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # аутефикация
            user=authenticate(request,username=username,password=password)
            if user:
                login1(request,user)
                return redirect("http://127.0.0.1:8000/")
    else:
        form=LoginForm()
    return render(request, 'object_detection/login.html',{'form': form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/login/")
    else:
        form = UserRegisterForm()
    return render (request, "object_detection/register.html",{"form": form})
    # return render(request,'object_detection/base.html')
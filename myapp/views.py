from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import CreateUserForm

def index(request):
    return HttpResponse('<h1>Hello World!</h1>')

def about(request):
    return HttpResponse('<h1>Hello Jasika!</h1>')

def user_login(request):
    context ={}
    return render(request, 'myapp/login.html',context)

def user_register(request):
    form = CreateUserForm()

    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request, 'myapp/register.html' , context)


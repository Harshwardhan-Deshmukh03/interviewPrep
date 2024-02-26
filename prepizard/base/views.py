from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect 
# Create your views here.

def home(request):
    return render(request,'base/home.html')


def login(request):
    context={}
    return render(request,'base/login.html',context)

def logout(request):
    context={}
    return HttpResponse("This is logout page")


def register(request):
    context={}
    return render(request,'base/register.html',context)


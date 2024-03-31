from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .utils import *
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


def onlineIDE(request):
    return render(request,'base/onlineIDE.html')
def land(request):
    return render(request,'base/landing_page.html')


def ide(request,pk):
    try:
        lang,lang_code,snippet=lookup(int(pk))
    except:
        return HttpResponse("Bad request")
    # return HttpResponse("This is ide of lang "+pk)

    if request.method=='POST':
         code = request.POST.get('code', '')
         input_data = request.POST.get('input', '')
         output=output_response_ide(lang_code,code,input_data)
         print(output)
         context={
            "pk":pk,
            "lang":lang,
            "lang_code":lang_code,
            "snippet":code,
            "input_data":input_data,
            "output":output,
            }
         return render(request,'base/ide.html',context)
    context={
        "pk":pk,
        "lang":lang,
        "lang_code":lang_code,
        "snippet":snippet,
        "input_data":"",
        "output":""

    }
    return render(request,"base/ide.html",context)
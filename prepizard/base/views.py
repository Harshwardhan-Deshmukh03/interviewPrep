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



# @unauthenticated_user
# def registerPage(request):
#     form=CreateUserForm()
#     if request.method=='POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user= form.save()
#             username=form.cleaned_data.get('username')
            
#             messages.success(request, "Account was created for "+username )
#             return redirect('login')
#     context={'form':form}
#     return render(request,'accounts/register.html',context)



# @unauthenticated_user
# def loginPage(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')


#         user=authenticate(request,username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             messages.info(request,"Username or password is incorrect")
#             return redirect('login')
#     context={}
#     return render(request,'accounts/login.html',context)



















def onlineIDE(request):
    return render(request,'base/onlineIDE.html')


def ide(request,pk):
    try:
        lang,lang_code,snippet=lookup(int(pk))
    except:
        return HttpResponse("Bad request")
    # return HttpResponse("This is ide of lang "+pk)

    if request.method=='POST':
         code = request.POST.get('code', '')
         input_data = request.POST.get('input', '')
         print(code)
         print(code.strip())
         output=output_response_ide(lang_code,code.strip(),input_data)
         print(output)
         context={
            "pk":pk,
            "lang":lang,
            "lang_code":lang_code,
            "snippet":code.strip(),
            "input_data":input_data,
            "output":output,
            }
         return render(request,'base/ide.html',context)
    context={
        "pk":pk,
        "lang":lang,
        "lang_code":lang_code,
        "snippet":snippet.strip(),
        "input_data":"",
        "output":""

    }
    return render(request,"base/ide.html",context)

def userhome(request):
    return render(request,'base/userhome.html')

def adminhome(request):
    return render(request,'base/adminhome.html')

def land(request):
    return render(request,'base/land.html')

def mcq(request):
    return render(request,'base/mcq.html')

def profile(request):
    return render(request,'base/profile.html')

def python(request):
    return render(request,'base/python.html')

def practice(request):
    return render(request,'base/practice.html')
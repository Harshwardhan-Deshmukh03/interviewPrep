from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .utils import *
from django.contrib import messages
from .decorators import *
from django.contrib.auth import authenticate,login,logout



# Create your views here.



# 

@login_required(login_url='login')
def home(request):
    return render(request,'base/home.html')


# def login(request):
#     context={}
#     return render(request,'base/login.html',context)



def register(request):
    context={}
    return render(request,'base/register.html',context)



# 


@unauthenticated_user
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        print(password)

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name
            if group == 'Admin':
                return redirect('adminhome')
            return redirect('userhome')
        else:
            messages.info(request,"Username or password is incorrect")
            return redirect('login')
    context={}
    return render(request,'base/login.html',context)







def logoutUser(request):
    logout(request)
    return redirect('login')









def mixide(request):
    return render(request, 'base/mixide.html')





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




# 

@login_required(login_url='login')
def userhome(request):
    return render(request,'base/userhome.html')



# 

@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def adminhome(request):
    return render(request,'base/adminhome.html')


def mcq(request):
    return render(request,'base/mcq.html')

def profile(request):
    return render(request,'base/profile.html')

def python(request):
    return render(request,'base/python.html')

def practice(request):
    return render(request,'base/practice.html')


def about(request):
    return render(request, 'about.html')

def resources(request):
    return render(request, 'resources.html')
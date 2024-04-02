from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .utils import *
from django.contrib import messages
from .decorators import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
from .models import *


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



@unauthenticated_user
def registerPage(request):
    if request.method == 'POST':
        # Get form data from the POST request
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        college = request.POST.get('college')
        password = request.POST.get('password')

        # Create the user manually
        user = User.objects.create_user(username=email, email=email, password=password)
        user.save()

        # Create the student instance
        student = Student.objects.create(
            user=user,
            name=name,
            phone=mobile,
            email=email,
            college=college
        )
        student.save()

        messages.success(request, "Account was created for " + email)
        return redirect('login')
    else:
        # Render the registration form
        return render(request, 'base/register.html')

# 


@unauthenticated_user
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
       
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






def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_description = request.POST.get('course_description')
        
        course = Course.objects.create(course_name=course_name, course_description=course_description)
        
        messages.success(request, "Course added successfully!")
        # Replace 'dashboard' with the name of your dashboard URL
        
    return render(request, 'base/add_course.html')






def add_question(request,pk):
    # Handle adding a question logic here
    if request.method == 'POST':
        # Retrieve course instance based on the pk
        course = Course.objects.get(pk=pk)
        # Extract form data
        question_text = request.POST.get('question_text')
        option1 = request.POST.get('option1')
        option2 = request.POST.get('option2')
        option3 = request.POST.get('option3')
        option4 = request.POST.get('option4')
        correct_option = request.POST.get('correct_option')

        # Create and save the Question instance
        question = Question.objects.create(
            course=course,
            question_text=question_text,
            option1=option1,
            option2=option2,
            option3=option3,
            option4=option4,
            correct_option=correct_option
        )

        # Optionally, you can add a success message
        messages.success(request, "Question added successfully!")

        # Redirect to a different page, such as the course detail page
        return redirect('add_question', pk=pk)





    courses = Course.objects.all()
    
    # Pass courses as context to the template
    context = {
        'courses': courses
    }
    return render(request, 'base/add_question.html',context )





def adminpractice(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request,'base/practice_admin.html',context )



def mixide(request):
    return render(request, 'base/mixide.html')





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
    return render(request, 'base/about.html')

def resources(request):
    return render(request, 'base/resources.html')


def adminabout(request):
    return render(request, 'base/adminabout.html')



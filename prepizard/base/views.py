from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect 
from .utils import *
from django.contrib import messages
from .decorators import *
from django.contrib.auth import authenticate,login,logout
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.models import User 
from .models import *
import io


# Create your views here.


@login_required(login_url='login')
def home(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request,'base/home.html',context )


# def login(request):
#     context={}
#     return render(request,'base/login.html',context)
from django.contrib.auth.models import User,Group
from django.contrib import messages
from .models import Student

def register(request):
    context = {}
    if request.method == 'POST':
        # Extract form data
        name = request.POST.get('nameSurname')
        email = request.POST.get('email')
        phone = request.POST.get('mobile')
        college = request.POST.get('college')
        password = request.POST.get('password')

        # Create a new user
        user = User.objects.create_user(username=email, email=email, password=password)
        group=Group.objects.get(name='User')
        user.groups.add(group)

        # Create and associate the student with the user
        student = Student.objects.create(
            user=user,
            name=name,
            email=email,
            phone=phone,
            college=college
        )

        # Optionally, add a success message
        messages.success(request, "Registration successful!")

        # Redirect the user to a different page (e.g., login page)
        return redirect('login')  # Replace 'login' with the name of your login URL pattern

    return render(request, 'base/register.html', context)



@unauthenticated_user
def registerPage(request):
    if request.method == 'POST':
        # Get form data from the POST request
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        college = request.POST.get('college')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.error(request, "User with this email already exists.")
            return render(request, 'base/register.html')
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
    student = Student.objects.get(user=request.user)
    higher_score_count = Student.objects.filter(score__gt=student.score).count()
    rank = higher_score_count + 1
    context = {
        'student': student,
        'rank':rank
    }
    # print(student.phone)
    return render(request,'base/profile.html',context )

def python(request):
    return render(request,'base/python.html')

def practice(request):
    return render(request,'base/practice.html')


def about(request):
    return render(request, 'base/about.html')

def resources(request):
    return render(request, 'base/resources.html')


def que(request):
    return render(request, 'base/que.html')



#Aarya's code :



from django.template.loader import get_template
from xhtml2pdf import pisa
import io
def generate_context(topic):
    if topic == 'DataScience':

       context = {
        'pageTitle': topic,
        'paragraph1': 'Data science is an interdisciplinary field that utilizes scientific methods, algorithms, processes, and systems to extract insights and knowledge from structured and unstructured data. It combines expertise from various domains such as mathematics, statistics, computer science, and domain-specific knowledge to analyze complex data sets and solve real-world problems. Data scientists leverage techniques such as data mining, machine learning, and predictive analytics to uncover patterns, trends, and correlations in data, enabling organizations to make data-driven decisions and gain a competitive edge in todays data-driven world.',
        'paragraph2': 'Data science is an interdisciplinary field that utilizes scientific methods, algorithms, processes, and systems to extract insights and knowledge from structured and unstructured data. It combines expertise from various domains such as mathematics, statistics, computer science, and domain-specific knowledge to analyze complex data sets and solve real-world problems. Data scientists leverage techniques such as data mining, machine learning, and predictive analytics to uncover patterns, trends, and correlations in data, enabling organizations to make data-driven decisions and gain a competitive edge in todays data-driven world.',
        'btnLink': 'http://127.0.0.1:8000/generate-pdf/DataScience',
        'btnText': 'Click Here'
         }
    elif topic == 'Programming':
       context = {
        'pageTitle': topic,
        'paragraph1': 'Programming is the process of creating a set of instructions that tell a computer how to perform a task. These instructions can be written in various programming languages, each with its syntax and semantics. Programmers use programming languages to develop software, websites, applications, and more.',
        'paragraph2': 'Programming is an essential skill in today\'s digital world, with demand for programmers in various industries such as technology, finance, healthcare, and entertainment.',
        'btnLink': 'http://127.0.0.1:8000/generate-pdf/Programming',
        'btnText': 'Click Here'
         }
    elif topic == 'Databases':
       context = {
        'pageTitle': topic,
        'paragraph1': 'A database is an organized collection of data, typically stored and accessed electronically from a computer system. Databases are essential components of modern information systems, used to store, manage, and retrieve data efficiently.',
        'paragraph2': 'There are various types of databases, including relational databases, NoSQL databases, and NewSQL databases, each designed for specific use cases and scalability requirements.',
        'btnLink': 'http://127.0.0.1:8000/generate-pdf/Databases',
        'btnText': 'Click Here'
         }
    elif topic == 'SystemDesign':
      context = {
        'pageTitle': topic,
        'paragraph1': 'System design is the process of defining the architecture, components, modules, interfaces, and data for a system to satisfy specified requirements. It is a multi-disciplinary field that encompasses software engineering, hardware engineering, network design, and more.',
        'paragraph2': 'System designers consider factors such as scalability, reliability, maintainability, performance, and security when designing systems for various applications and industries.',
        'btnLink': 'http://127.0.0.1:8000/generate-pdf/SystemDesign',
        'btnText': 'Click Here'
       }

    return context

def cheatsheet(request,topic):
    # context = {
    #     'pageTitle': 'Data Science',
    #     'paragraph1': 'Data science is an interdisciplinary field that utilizes scientific methods, algorithms, processes, and systems to extract insights and knowledge from structured and unstructured data. It combines expertise from various domains such as mathematics, statistics, computer science, and domain-specific knowledge to analyze complex data sets and solve real-world problems. Data scientists leverage techniques such as data mining, machine learning, and predictive analytics to uncover patterns, trends, and correlations in data, enabling organizations to make data-driven decisions and gain a competitive edge in todays data-driven world.',
    #     'paragraph2': 'Data science is an interdisciplinary field that utilizes scientific methods, algorithms, processes, and systems to extract insights and knowledge from structured and unstructured data. It combines expertise from various domains such as mathematics, statistics, computer science, and domain-specific knowledge to analyze complex data sets and solve real-world problems. Data scientists leverage techniques such as data mining, machine learning, and predictive analytics to uncover patterns, trends, and correlations in data, enabling organizations to make data-driven decisions and gain a competitive edge in todays data-driven world.',
    #     'btnLink': 'http://127.0.0.1:8000/generate-pdf/',
    #     'btnText': 'Click Here'
    # }
    
    context = generate_context(topic)
    return render(request, 'base/cheatsheet.html', context)



def generate_pdf(request,topic):
    # Render the HTML template
    template = get_template('base/cheatsheet.html')
    string = topic
    context = generate_context(string)
    html = template.render(context)

    # Create a PDF file
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), result)

    # Return PDF as response
    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="my_website.pdf"'
        return response
    return HttpResponse('Error rendering PDF', status=500)


def resources(request):
    topics = ["DataScience", "Programming", "Databases", "SystemDesign"]  # Define your topic string array here
    context = {'topics': topics}  # Create a dictionary with 'topics' key and the array as its value
    return render(request, 'base/resources2.html', context)  # Pass the context dictionary when rendering the template


# def resources(request):
#     return render(request, 'base/base/resources2.html')


def que(request):
    return render(request, 'base/que.html')



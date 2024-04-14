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
<<<<<<< HEAD
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

def create_resource(resource_name, resource_description, resource_material):
    try:
        resource = Resource.objects.create(
            resource_name=resource_name,
            resource_description=resource_description,
            resource_material=resource_material
        )
        return resource  # Return the created resource instance if successful
    except Exception as e:
        # Handle exceptions, such as IntegrityError if resource_name violates unique constraint
        print(f"Error creating resource: {e}")
        return None



create_resource('DataSci','Data science is an interdisciplinary field that utilizes scientific methods, algorithms, processes, and systems to extract insights and knowledge from structured and unstructured data. It combines expertise from various domains such as mathematics, statistics, computer science, and domain-specific knowledge to analyze complex data sets and solve real-world problems. Data scientists leverage techniques such as data mining, machine learning, and predictive analytics to uncover patterns, trends, and correlations in data, enabling organizations to make data-driven decisions and gain a competitive edge in todays data-driven world.','Data science is an interdisciplinary field that utilizes scientific methods, algorithms, processes, and systems to extract insights and knowledge from structured and unstructured data. It combines expertise from various domains such as mathematics, statistics, computer science, and domain-specific knowledge to analyze complex data sets and solve real-world problems. Data scientists leverage techniques such as data mining, machine learning, and predictive analytics to uncover patterns, trends, and correlations in data, enabling organizations to make data-driven decisions and gain a competitive edge in todays data-driven world.')
# create_resource('Programming', 'resource_description', 'resource_material')
# create_resource('Databases', 'resource_description', 'resource_material')
# create_resource('SystemDesign', 'resource_description', 'resource_material')

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
    context = get_resource_context(topic)
    #context = generate_context(topic)
    return render(request, 'base/cheatsheet.html', context)



def generate_pdf(request,topic):
    # Render the HTML template
    template = get_template('base/cheatsheet.html')

    context = get_resource_context(topic)
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


# def resources(request):
#     topics = ["DataScience", "Programming", "Databases", "SystemDesign"]  # Define your topic string array here
#     context = {'topics': topics}  # Create a dictionary with 'topics' key and the array as its value
#     return render(request, 'base/resources2.html', context)  # Pass the context dictionary when rendering the template

from .models import Resource  # Import the Resource model

def resources(request):
    # Retrieve all resource names from the Resource model
    resources = Resource.objects.values_list('resource_name', flat=True)
    
    # Convert the queryset to a list
    topics = list(resources)
    
    context = {'topics': topics}  # Create a dictionary with 'topics' key and the list of resource names as its value
    return render(request, 'base/resources2.html', context)  # Pass the context dictionary when rendering the template


# def resources(request):
#     return render(request, 'base/base/resources2.html')


def que(request):
    return render(request, 'base/que.html')


#####
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import render, redirect 
# from .utils import *
# from django.contrib import messages
# from .decorators import *
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.models import User 
# from .models import *
=======
from django.utils.text import slugify
>>>>>>> origin/dev_shravani


# Create your views here.



# 

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

        if not course_name or not course_description:
            messages.error(request, "Both course name and description are required.")
            return redirect('adminpractice')
        
        course = Course.objects.create(course_name=course_name, course_description=course_description)
        room_name = course_name
        slug = slugify(course_name)
        room = Room.objects.create(name=room_name, slug=slug)
        
        messages.success(request, "Course added successfully!")
        # Replace 'dashboard' with the name of your dashboard URL
        return redirect('adminpractice')
        
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

        if not question_text or not option1 or not option2 or not option3 or not option4 or not correct_option:
            # Add an error message if any field is missing
            messages.error(request, "All fields are required.")
            return redirect('add_question', pk=pk)

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





def practice(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request,'base/practice.html',context)






def coursequestion(request, pk):
    course = Course.objects.get(pk=pk)
    questions = Question.objects.filter(course=course)
    
    # Get attempts for the current user
    user = request.user.student
    attempts = Attempt.objects.filter(student=user, question__in=questions)
    
    # Create a dictionary to store question IDs and attempts
    question_attempt_map = []
    for attempt in attempts:
        # print(attempt.question.id)
        question_attempt_map.append(attempt.question.id)
    
    context = {
        'course': course,
        'questions': questions,
        'question_attempt_map': question_attempt_map,
    }
    return render(request, 'base/course_question.html', context)






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


def about(request):
    return render(request, 'base/about.html')

# def resources(request):
#     return render(request, 'base/resources.html')


def adminabout(request):
    return render(request, 'base/adminabout.html')

def add_resource(request):
    if request.method == 'POST':
        resource_name = request.POST.get('resource_name')
        resource_description = request.POST.get('resource_description')
        resource_material = request.POST.get('resource_material')
        
        resource = Resource.objects.create(
            resource_name=resource_name,
            resource_description=resource_description,
            resource_material=resource_material
        )
        
        messages.success(request, "Resource added successfully!")
    return render(request, 'base/add_resource.html')


def adminresource(request):
    resources = Resource.objects.all()
    context = {
        'resources': resources
    }
    return render(request,'base/resource_admin.html',context )



def show_question(request, pk):
    question = Question.objects.get(pk=pk)
    
    if request.method == 'POST':
        selected_option = request.POST.get('selected_option')
        
        # Determine if the question has been attempted by the current user
        user = request.user.student
        print(user)
        attempted = Attempt.objects.filter(student=user, question=question).exists()
        
        if attempted:
            # User has already attempted the question, do not process the answer again
            messages.error(request, "You've already attempted this question.")
            if int(selected_option) == question.correct_option:
                messages.success(request,"You have correctly answered question.")
            else:
                messages.error(request, "Wrong answer.")
            return redirect('que', pk=pk)
        else:
            # Create a new attempt object to store the user's answer
            attempt = Attempt(student=user, question=question)
            attempt.attempted = True
            
            # Check if the selected option is correct
            if int(selected_option) == question.correct_option:
                attempt.correct_attempt = True
                # Increase the user's score if the answer is correct
                user.score += 1
                user.save()
                messages.success(request,"You have correctly answered question. You have earned a point. ")
                return redirect('que',pk=pk)
            else:
                attempt.correct_attempt = False
                messages.error(request, "Wrong answer.")
                return redirect(show_question,pk=pk)

            
            attempt.save()
            
            # Redirect to the same question page after processing the answer
            return redirect('que', pk=pk)
    
    # If it's a GET request, render the question page as usual
    attempted_attempt = Attempt.objects.filter(student=request.user.student, question=question).first()
    attempted = attempted_attempt is not None
    correct_attempt = attempted_attempt.correct_attempt if attempted_attempt else False
    
    context = {
        'question': question,
        'attempted': attempted,
        'correct_attempt': correct_attempt,  # Pass the 'correct_attempt' variable to the template
    }
    print(context)
    return render(request, 'base/que.html', context)








def forums(request):
    rooms=Room.objects.all()
    return render(request,'base/forums.html',{'rooms':rooms})


def room(request,slug):
    room=Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room).order_by('-date_added')[:50][::-1]
    return render(request,'base/room.html',{'room':room,'messages':messages})


# FORUMULA SHEETS





def add_sheet(request):
    if request.method == 'POST':
        topic_name = request.POST.get('topic_name')
        description = request.POST.get('description')
        pdf_file = request.FILES.get('pdf_file')  # Assuming file input name is 'pdf_file'
        print(topic_name,description)
        if topic_name and pdf_file:
            cheatsheet = CheatSheet.objects.create(
                topic_name=topic_name,
                description=description,
                pdf_file=pdf_file
            )
            messages.success(request, "Cheat sheet added successfully!")
        else:
            messages.error(request, "Please fill in all required fields.")
        return redirect('adminsheet')

    return render(request, 'base/addsheet.html')








def adminsheet(request):
    cheatsheets = CheatSheet.objects.all()
    for sheet in cheatsheets:
        print(sheet.pdf_file)
    context = {
        'cheatsheets': cheatsheets
    }
    return render(request, 'base/adminsheet.html', context)




def usersheet(request):
    cheatsheets = CheatSheet.objects.all()
    for sheet in cheatsheets:
        print(sheet.pdf_file)
    context = {
        'cheatsheets': cheatsheets
    }
    return render(request, 'base/usersheet.html', context)










from .models import Resource

def get_resource_context(input_string):
    try:
        resource = Resource.objects.filter(resource_name=input_string).first()
        context = {
            'pageTitle': resource.resource_name,
            'paragraph1': resource.resource_description,
            'paragraph2': resource.resource_description,  # You can modify this if needed
            'btnLink': f'http://127.0.0.1:8000/generate-pdf/{input_string}',
            'btnText': 'Click Here'
        }
        return context
    except Resource.DoesNotExist:
        return None  # Return None if no resource found for the input string

from .models import Resource



from django.shortcuts import render

#aarya edit
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("HomePage")
def contact(request):
    return render(request,'MYAPP/dashboard.html')



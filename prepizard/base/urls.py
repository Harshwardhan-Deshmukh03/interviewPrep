from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('',views.userhome,name="userhome"),
    path('adminhome/',views.adminhome,name="adminhome"),

    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('register/',views.register,name="register"),




    path('onlineIDE/',views.onlineIDE,name="onlineIDE"),
    path('ide/<str:pk>/',views.ide,name="ide"),
    


    
    path('mcq/' , views.mcq ,name = "mcq"),
    path('profile/' , views.profile ,name = "profile"),

    path('python/' , views.python ,name = "python"),
    path('practice/' , views.practice ,name = "practice"),
    

    
]


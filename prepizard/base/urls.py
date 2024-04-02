from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('',views.userhome,name="userhome"),
    path('adminhome/',views.adminhome,name="adminhome"),

    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    path('register/',views.register,name="register"),




    path('onlineIDE/',views.onlineIDE,name="onlineIDE"),
    path('ide/<str:pk>/',views.ide,name="ide"),


    path('mixide/',views.mixide,name="mix"),
    path('adminhome/mixide/',views.mixide,name="mixide"),
    # path('idecomb/',views.idecomb,name="comb"),
    



    path('mcq/' , views.mcq ,name = "mcq"),
    path('profile/' , views.profile ,name = "profile"),
    path('adminpractice/' , views.adminpractice ,name = "adminpractice"),
    path('adminresource/' , views.adminresource ,name = "adminresource"),

     path('add_course/', views.add_course, name='add_course'),
     path('add_resource/', views.add_resource, name='add_resource'),
    path('add_question/<str:pk>', views.add_question, name='add_question'),

    path('python/' , views.python ,name = "python"),
    path('practice/' , views.practice ,name = "practice"),
    path('about/', views.about, name='about'),
    path('about/', views.resources, name='resources'),
    path('adminabout/', views.adminabout, name='adminabout'),
    path('resources/', views.resources, name='resources'),
    path('que/', views.que, name='que'),
 
]


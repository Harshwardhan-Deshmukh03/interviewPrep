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
    path('questions/<int:pk>', views.coursequestion, name='course_question'),

    path('python/' , views.python ,name = "python"),
    path('practice/' , views.practice ,name = "practice"),
    path('about/', views.about, name='about'),
    path('about/', views.resources, name='resources'),
    path('adminabout/', views.adminabout, name='adminabout'),
    path('resources/', views.resources, name='resources'),
    # path('que/', views.que, name='que'),
 
    
    path('que/<int:pk>', views.show_question, name='que'),
    path('forums/', views.forums, name='forums'),
    path('room/<slug:slug>', views.room, name='room'),

    #Aarya's code :
    path('add_sheet/', views.add_sheet, name='addsheet'),
    path('adminsheet/', views.adminsheet, name='adminsheet'),
    path('usersheet/', views.usersheet, name='usersheet'),
    path('cheatsheet/<str:topic>/', views.cheatsheet, name='cheatsheet'),
    path('generate-pdf/<str:topic>/', views.generate_pdf, name='generate_pdf'),

    

    
]


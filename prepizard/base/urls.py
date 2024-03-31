from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('',views.home,name="home"),

    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('register/',views.register,name="register"),
   #aarya
    path('landingpage/',views.land,name="land"),


    path('onlineIDE/',views.onlineIDE,name="onlineIDE"),
    path('ide/<str:pk>/',views.ide,name="ide"),
    

    
]


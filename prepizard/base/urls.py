from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('',views.home,name="home"),

    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('register/',views.register,name="register"),



    path('onlineIDE/',views.onlineIDE,name="onlineIDE"),
    path('ide/<str:pk>/',views.ide,name="ide"),
    #added new
    path('land/' , views.land ,name = "land"),
    

    
]


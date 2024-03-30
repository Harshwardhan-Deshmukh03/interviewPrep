from django.urls import path
from . import views
urlpatterns = [

    path('',views.home),
    path('contact/',views.contact),
    path('contact2/',views.contact2),

]

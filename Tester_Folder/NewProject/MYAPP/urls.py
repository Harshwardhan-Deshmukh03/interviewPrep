from django.urls import path
from . import views
from .views import generate_pdf
urlpatterns = [

    path('',views.home),
    path('contact/',views.contact),
    path('contact2/',views.contact2),
    path('index/', views.index, name='index'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
]


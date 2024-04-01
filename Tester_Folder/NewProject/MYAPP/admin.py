from django.contrib import admin

# Register your models here.

# forms.py
from django import forms



class MyForm(forms.Form):
    name = forms.CharField(label='Name', initial='John Doe', widget=forms.Textarea)
    age = forms.CharField(label='Age', initial=30, widget=forms.Textarea)

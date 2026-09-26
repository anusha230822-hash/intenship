from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def students_home(request):
    return HttpResponse("Welcome to Students Page")

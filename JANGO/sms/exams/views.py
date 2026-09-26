from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def exams_home(request):
    return HttpResponse("Welcome to Exams Page")




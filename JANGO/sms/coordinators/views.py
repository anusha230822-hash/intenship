from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def coordinators_home(request):
    return HttpResponse("Welcome to Coordinators Page")



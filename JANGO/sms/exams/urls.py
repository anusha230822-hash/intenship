from django.urls import path
from . import views

urlpatterns = [
    path('', views.exams_home ,name='exams_home'),
]
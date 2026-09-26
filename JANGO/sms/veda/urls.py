from django.urls import path
from . import views

urlpatterns = [
    path('', views.veda_home ,name='veda_home'),
]
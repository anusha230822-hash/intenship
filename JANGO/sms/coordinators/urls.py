from django.urls import path
from . import views

urlpatterns = [
    path('', views.coordinators_home ,name='coordinators_home'),
]
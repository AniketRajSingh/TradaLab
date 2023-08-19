from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('', views.apply_for_internship, name='apply_for_internship'),
]

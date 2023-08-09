from django.urls import path
from . import views

urlpatterns = [
    path('', views.lab_home, name='lab_home'),
    path('<str:standard>/<str:subject>/', views.lab_page, name='lab_page'),
    path('<str:standard>/<str:subject>/<int:experiment_id>/', views.lab_experiment_detail, name='lab_experiment_detail'),
]

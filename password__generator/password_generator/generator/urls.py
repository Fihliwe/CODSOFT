from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_password, name='generate_password'),
]

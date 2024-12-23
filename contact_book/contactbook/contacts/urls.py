from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('<int:pk>/', views.contact_detail, name='contact_detail'),
    path('add/', views.contact_create, name='contact_create'),
    path('<int:pk>/edit/', views.contact_update, name='contact_update'),
    path('<int:pk>/delete/', views.contact_delete, name='contact_delete'),
]

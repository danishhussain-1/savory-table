"""
URL configuration for the Menu app.

Namespace: 'menu'
"""
from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list_view, name='menu_list'),
    path('<slug:slug>/', views.menu_detail_view, name='menu_detail'),
]
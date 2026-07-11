"""
URL configuration for the Reservations app.

Namespace: 'reservations'
"""
from django.urls import path

from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.reservation_create_view, name='reservation_create'),
    path('my-reservations/', views.my_reservations_view, name='my_reservations'),
    path('cancel/<int:pk>/', views.cancel_reservation_view, name='cancel_reservation'),
]
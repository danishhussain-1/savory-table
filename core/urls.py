"""
URL configuration for the Core app.

Namespace: 'core'
"""
from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('newsletter/subscribe/', views.newsletter_signup_view, name='newsletter_signup'),
]
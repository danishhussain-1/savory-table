"""
URL configuration for the Accounts app.

Namespace: 'accounts'
"""
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.StyledLoginView.as_view(), name='login'),
    path('logout/', views.StyledLogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
]
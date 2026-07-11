"""
URL configuration for the Reviews app.

Namespace: 'reviews'
"""
from django.urls import path

from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.review_list_view, name='review_list'),
    path('submit/', views.submit_review_view, name='submit_review'),
    path('submit/<slug:slug>/', views.submit_menu_item_review_view, name='submit_menu_item_review'),
]
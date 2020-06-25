"""
Definition of urls for TransCo.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('quickquote', views.quickquote, name='quickquote'), 
    path('gallery/', views.gallery, name='gallery'),
    path('admin/', admin.site.urls),
]

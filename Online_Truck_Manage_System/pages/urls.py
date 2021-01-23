from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('',views.home_view, name='home'),
    path('contact/',views.contact_view, name='contact'),
    path('about/',views.about_view, name='about'),
    path('projects/',views.about_view, name='projects') 
    ]

from django.contrib import admin
from django.urls import path
from . import views

app_name = 'vehicles'

urlpatterns = [
    path('create/',views.create_vehicle_details, name='create'),
    path('truck/',views.vehicle_view, name='truck'),
    path('dashboard/',views.get_all_vehicle_view, name='truck_details')
]

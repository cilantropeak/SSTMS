from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Vehicle(models.Model):
    Date = models.DateField(default=timezone.now)
    vechicle_no = models.IntegerField(default=6)
    start_meter_reading = models.FloatField()
    desile_filling = models.FloatField()
    trips = models.IntegerField()
    end_meter_reading = models.FloatField()
    instructions = models.CharField(max_length=100,default="Available")
    image = models.ImageField(default='default.png', upload_to='images/')
    slug = models.SlugField(default="vno")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250,blank=True)
    
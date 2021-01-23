from django import forms
from .models import Vehicle
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone

class VechicleForm1(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [            
            'Date',
            'vechicle_no', 
            'start_meter_reading',
            'desile_filling',
            'trips',
            'end_meter_reading',
            'instructions',
            'image',
            'slug',
            'created_by',
            'title',
        ]
class VechicleForm(forms.ModelForm):
    instructions = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Please add comments"}))
   # Date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'], widget=forms.DateTimeInput(attrs={'type':'date'}))
    Date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    vechicle_no = forms.CharField(widget=forms.NumberInput(attrs={"placeholder":"Please add Lorry Number Ex: L1234"}))
    start_meter_reading = forms.CharField(widget=forms.NumberInput(attrs={"placeholder":"Please add Start Meter Reading Ex: 7998"}))
    end_meter_reading = forms.CharField(widget=forms.NumberInput(attrs={"placeholder":"Please add End Meter Reading Ex: 8999"}))
    desile_filling = forms.CharField(widget=forms.NumberInput(attrs={"placeholder":"Please enter desile filling in liters Ex: 123"}))
    trips = forms.CharField(widget=forms.NumberInput(attrs={"placeholder":"Please enter how many Trips today Ex: 5"}))
    class Meta:
        model = Vehicle
        fields = [            
            'Date',
            'vechicle_no', 
            'start_meter_reading',
            'desile_filling',
            'trips',
            'end_meter_reading',
            'instructions',
        ]

class VechicleRawForm(forms.Form):
     Date = forms.DateField()
     vechicle_no = forms.IntegerField()
     start_meter_reading = forms.DecimalField(initial=0)
     desile_filling = forms.FloatField(initial=0)
     trips = forms.IntegerField(initial=0)
     end_meter_reading = forms.FloatField()
     instructions = forms.CharField(initial='This lorry is new awsome')
     image = forms.ImageField(label='Lorry Image',)
     title = forms.CharField(label='Lorry Title')
     description = forms.CharField()

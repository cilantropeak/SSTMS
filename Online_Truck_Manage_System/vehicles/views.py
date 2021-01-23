from django.shortcuts import render
from .models import Vehicle
from .forms import VechicleForm, VechicleRawForm
# Create your views here.
def vehicle_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    vehicleObj = Vehicle.objects 
    my_context = {
        "vehicles" : vehicleObj
    }
    return render(request,'vehicles/vehicle_details.html',my_context)

def get_all_vehicle_view(request, *args, **kwargs):
    print('Inside vehicles details ::')
    vehicleObj = Vehicle.objects.all()
    my_context = {
        "vehicles" : vehicleObj
    }
    return render(request,'vehicles/vehicle_details.html',my_context)

def create_vehicle_details(request):
    print('@@@@@@@@@@ inside create_vehicle_details ')
    form = VechicleForm(request.POST or None)
    print('@@@@@@@@@@ inside create_vehicle_details ',form)
    if form.is_valid():
        Vehicle = form.save(commit=False)
        Vehicle.created_by = request.user
        Vehicle = form.save()
        #form.save()
        form = VechicleForm()
    else:
        print('@@@@@@@ form is not valid')
    my_context = {
        'form' :form
    }
    return render (request,"vehicles/create_vehicle_details.html", my_context)

def create_vehicle_details1(request):
    my_form = VechicleRawForm()
    if request.method == "POST":
        my_form = VechicleRawForm(request.POST or None)
        if my_form.is_valid():
            Vehicle.objects.create(**my_form.cleaned_data)
           # my_form.save()
            my_form = VechicleForm()
        else:
            print(my_form.errors)

    my_context = {
        'form' :my_form
    }
    return render (request,"vehicles/create_vehicle_details.html", my_context)
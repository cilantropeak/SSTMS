from django.shortcuts import render

# Create your views here.
def contact_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return render(request,'pages/contact.html',{})

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return render(request,'pages/home.html',{})

def about_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return render(request,'pages/about.html',{})

def projects_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    return render(request,'pages/projects.html',{})
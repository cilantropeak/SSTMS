# Create your views here.
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import NewUSerForm, NewUSerForm_new


def signup_view(request):
    if request.method == 'POST':
        form = NewUSerForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pages:home')
    else:
        form = NewUSerForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        print('req obj ', request)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('vehicles:truck_details')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login_new')


def login_view_1(request):
    if request.method == 'POST':
        print('req obj ', request)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('vehicles:truck_details')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login_1.html', {'form': form})


def login_view_new(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('@@@@@@@@@@@@@@@@ username ::  ', username)
        print('@@@@@@@@@@@@@@@@ password ::  ', password)
        user = authenticate(username=username, password=password)
        print('@@@@@@@@@@@@@@@@ USER ::  ', user)
        if user is not None:
            if user.is_active:
                login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('vehicles:truck_details')
    # return render_to_response('login.html', context_instance=RequestContext(request))
    else:
        user = AuthenticationForm()
    return render(request, 'accounts/login_new.html', {'form': user})


def signup_view_temp(request):
    print('signup_view_temp ??????? :: ', request)
    if request.method == 'POST':
        print('signup_view_temp :: ', request)
        form = NewUSerForm_new(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vehicles:truck_details')
    else:
        form = NewUSerForm_new()
    #return render(request, 'vehicles/truck_details', {})
    return redirect('vehicles:truck_details')

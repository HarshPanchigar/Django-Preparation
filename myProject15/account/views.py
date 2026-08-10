from django.shortcuts import render , redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request,'register successfully and logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'registeration faild. please correct the errors below')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form' : form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'Login Successfully')
            return redirect('dashboard')
        else:
            messages.error(request,'invalid username or password')
    return render(request,'account/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,'you have been logout.')
    return redirect('login')

def dashboard_view(request):
    return render(request, 'account/dashboard.html')
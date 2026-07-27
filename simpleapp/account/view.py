from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request , 'signup.html' , {'error' : "user already exists"})

        User.objects.create_user(username=username , password=password)
        return redirect('login')
    
    return render(request , 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username , password= password)

        if user:
            login(request,user)
            return redirect('home')

        return render(request , 'login.html' , {'error':'invalid credentials'})

    return render(request , 'login.html')

def home(request):
    if not request.user.is_authenticated:
        redirect('login')
    return render(request , 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')
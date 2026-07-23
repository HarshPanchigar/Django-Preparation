from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to blog home page!")

def about(request):
    ans = 20 + 20
    return HttpResponse(f'<h1>About page: {ans}</h1>')
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Shop home page</h1>")

def product(request):
    return HttpResponse('<h1>Shop product page</h1>')
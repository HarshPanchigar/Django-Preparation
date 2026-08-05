from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contect

def contect_form(request):
    return render(request , 'contect.html')

def submit_contect(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')

        if name and message:
            Contect.objects.create(name=name,message=message)
            return HttpResponse(f"Thank you {name} ,for your message...")
        else:
            return HttpResponse('please provide name and meassage')
    return redirect('contect_form')
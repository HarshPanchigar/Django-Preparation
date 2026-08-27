from django.shortcuts import render
from django.http import HttpResponse

def fun1(request):
    return HttpResponse('hello function base view')

def fun2(request):
    return HttpResponse('<h1>hello function base view</h1>')

def homefun(request):
    return render(request,'home.html')

def aboutfun(request):
    context = {'msg' : 'welcome to about us page'}
    return render(request, 'about.html' ,context)

def newsfun(request):
    template_name = 'news.html'
    context = {'info' : 'this page is load from url'}
    return render(request, template_name ,context)

def newsfun(request, template_name):
    template_name = template_name
    context = {'info' : 'this page is load from url of the urls page'}
    return render(request, template_name ,context)

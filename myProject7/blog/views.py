from django.shortcuts import render
from datetime import datetime

def home(request):
    blog = [
        {"title" : "django basic","is_featured" : True,"author" : 'harsh panchigar'},
        {"title" : "django advanced","is_featured" : False,"author" : ''},
        {"title" : "django rest framwork","is_featured" : False,"author" : 'john snow'}

    ]
    context = {
        'blogs' : blog,
        'today' : datetime.now(),
        "html_code" : "<h1>welcome to my blog.</h1>"
    }
    return render(request, 'blog.html',context)
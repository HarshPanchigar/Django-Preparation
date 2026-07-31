from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    post = {
        "title" : "my first post",
        "description" : "Django is high level python web framwork",
        "author" : "harsh",
        "Created_at" : datetime.now(),
        "comment_count" : 2,
        "tags" : ["django" , "Python" ,'web framwork'],
        "price" : 100,
        "number" : 2,
    }
    return render(request , 'blog_details.html' , {'post' : post})
from django.shortcuts import render
from datetime import datetime
# Create your views here.

class User:
    def __init__(self , name ,age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18

def home(request):
    context = {
        'name' : 'Harsh',
        'age' : 21,
        'skill' : ['Python' , 'Django' , 'FastAPI'],
        'user' : User("Panchigar" , 20),
        'blog' : {
            "title" : "Django template Intro",
            'auther' : {
                'name' : "harsh panchigar",
            },
            "contect" : "<b>Harshpanchigar@gmail.com</b>",
            "created_at" : datetime(2026,7,28,20,30) 
        },
        'empty_value' : None,
    }
    return render(request , "home.html" , context )
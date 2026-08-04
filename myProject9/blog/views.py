from django.shortcuts import render
from .models import Student

def blog(request):
    students = Student.objects.all()
    return render(request,'blog.html' , {'students' : students})
from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class StudentViweSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
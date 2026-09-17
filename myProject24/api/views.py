from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Student
from .serializers import StudentSerializer

class StudentList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class StudentDelete(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self, request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)

    
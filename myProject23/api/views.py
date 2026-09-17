from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

#CRUD opration APIView
class StudentAPI(APIView):
    #read all or single data
    def get(self,request,pk=None):
        if pk:
            try:
                student = Student.objects.get(id=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except student.DoesNotExist:
                return Response({'error' : 'student not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            #read all data
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

#create data(post)
    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #put api
    def put(self,request,pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({'error':'Student not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data ,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete api
    def delete(self,request,pk):
        try:
            student = Student.objects.get(id=pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({'error':'student not found'},status=status.HTTP_404_NOT_FOUND)
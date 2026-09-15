from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET'])
def get_student(requset):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_student(requset):
    serializer = StudentSerializer(data = requset.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','PATCH'])
def update_student(requset,id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response({"error":"Student does not found"},status=status.HTTP_404_NOT_FOUND)

    if requset.method == 'PATCH':
        serializer = StudentSerializer(student,data=requset.data ,partial=True)
    else:
        serializer = StudentSerializer(student, data=requset.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_student(requset,id):
    try:
        student = Student.objects.get(id=id)
    except:
        return Response({'error' : 'student not found'}, status=status.HTTP_404_NOT_FOUND)

    student.delete()
    return Response({'message' : 'student deleted successfully'} , status=status.HTTP_204_NO_CONTENT)

from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('students/', StudentAPI.as_view()), #For get all data and post
    path('students/<int:pk>', StudentAPI.as_view()), #For get single data , put and delete
]

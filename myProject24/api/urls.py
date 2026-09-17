from django.urls import path
from .views import StudentList,StudentDelete

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('students/<int:pk>',StudentDelete.as_view())
]

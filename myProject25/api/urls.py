from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViweSet

route = DefaultRouter()
route.register('student', StudentViweSet, basename='student')

urlpatterns = [
    path('', include(route.urls))
]

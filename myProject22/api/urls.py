from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.get_student, name='get_student'),
    path('student/add', views.add_student, name='add_student'),
    path('student/put/<int:id>', views.update_student, name='update_student'),
    path('student/delete/<int:id>', views.delete_student, name='delete_student'),
]
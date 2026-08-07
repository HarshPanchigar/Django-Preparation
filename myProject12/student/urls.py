from . import views
from django.urls import path

urlpatterns = [
    path("", views.student_list, name='student_list'),
    path('add/' , views.student_create , name='student_create'),
    path('details/<int:pk>' , views.student_detail , name='student_detail'),
    path('edit/<int:pk>' , views.student_edit , name='student_edit'),
    path('delete/<int:pk>' , views.student_delete , name='student_delete'),
]


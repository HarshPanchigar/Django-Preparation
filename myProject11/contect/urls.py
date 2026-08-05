from . import views
from django.urls import path

urlpatterns = [
    path('', views.contect_form , name='contect_form'),
    path('submit/' , views.submit_contect, name='submit_contect')
]

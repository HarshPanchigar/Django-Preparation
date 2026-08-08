from . import views
from django.urls import path

urlpatterns = [
    path('' , views.show_msg , name='show_msg')
]

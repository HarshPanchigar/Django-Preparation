from . import views
from django.urls import path

urlpatterns = [
    path('shop/',views.home , name='shop'),
    path('product/', views.product , name='products')
]
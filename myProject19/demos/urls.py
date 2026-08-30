from django.urls import path
from . import views

urlpatterns = [
    path('',views.fun1,name='fun1'),
    path('fun2/', views.fun2, name='fun2'),
    path('home/', views.homefun, name='homefun'),
    path('about/', views.aboutfun, name='aboutfun'),
    path('news/', views.newsfun, name='newsfun'),
    path('news/', views.newsfun, {'template_name' : 'news.html'} , name='newsfun'),
]
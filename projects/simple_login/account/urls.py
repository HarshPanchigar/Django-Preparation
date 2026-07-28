from . import views
from django.urls import path

urlpatterns = [
    path('' , views.login_view , name='login'),
    path('home/' , views.home , name='home'),
    path('signup/' , views.signup , name='signup'),
    path('logout/' , views.logout_view , name='logout'),
]
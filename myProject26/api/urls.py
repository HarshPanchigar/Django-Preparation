from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



# urlpatterns = [
#     path('public/', views.public_view, name='public_view'),
#     path('private/', views.privat_view, name='privat_view'),   
# ]

urlpatterns = [
    path('get-token/', obtain_auth_token, name='api_token_auth'),
    path('profile/', views.user_profile, name='user_profile'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]

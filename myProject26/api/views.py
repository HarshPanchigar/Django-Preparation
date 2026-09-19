# from django.shortcuts import render
# from rest_framework.decorators import api_view, permission_classes, authentication_classes
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny  

# @api_view(['GET'])
# @authentication_classes([])
# @permission_classes([AllowAny])
# def public_view(request):
#     return Response({'message' : 'This is public view accessable to evryone'})

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def privat_view(request):
#     return Response({'message':f'hello, {request.user.username}. This is private access'})

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

#api for only authenticated person
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    return Response({
        'username' : user.username,
        'email' : user.email,
        'is_staff' : user.is_staff,
    })

#api for only admin user
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin_panel(request):
    return Response({"message" : f"Welcome to the admin panel !,{request.user.username}"})

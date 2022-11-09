from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib import messages
from .serializers import UserSerializer

# Create your views here.


@api_view(['POST'])
def login_user(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response("User logged in", status=status.HTTP_200_OK)
    else:
        messages.success(request, "No such user exists, please sign up.")
        return Response("User doesn't exist", status=status.HTTP_200_OK)


@api_view(['GET'])
def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return Response("User logged out", status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user(request):
    new_user = UserSerializer(data=request.data)
    if new_user.is_valid():
        user_saved = new_user.save()
        return Response('User {} created'.format(user_saved.username), status=status.HTTP_200_OK)
    else:
        return Response('User not created', status=status.HTTP_200_OK)


# @api_view(['GET'])
# def see_user(request):
#     username = User.username
#     return Response(user)

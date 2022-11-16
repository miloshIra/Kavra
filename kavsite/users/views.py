from django.shortcuts import render, redirect
import hashlib
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib import messages
from .serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.


@api_view(['POST'])
def login_user(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    print(user)
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


@api_view(['GET'])
def get_all_users(request):
    User = get_user_model()
    users = User.objects.values()
    context = {'users': users}
    return Response(context, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_user(request):
    new_user = UserSerializer(data=request.data)
    if new_user.is_valid():
        user_saved = new_user.create(request.data)
        return Response('User {} created'.format(user_saved.username), status=status.HTTP_200_OK)
    else:
        return Response('User not created', status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_user(request):
    user = User.objects.get(id=request.data['id'])
    user.delete()
    return Response('User deleted')


# @api_view(['GET'])
# def see_user(request):
#     username = User.username
#     return Response(user)

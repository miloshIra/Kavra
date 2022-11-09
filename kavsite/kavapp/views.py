from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib import messages
from .serializers import RecipeSerializer
from .models import Recipe
from django.core.exceptions import ValidationError

# Create your views here.


@api_view(['POST'])
def create_recipe(request):
    """ Creates a new recipe ... at least it should .. if it works it's django magic."""
    data = request.data
    data['user'] = request.user.id
    # print(data)
    new_recipe = RecipeSerializer(data=data)
    # print(request.user.email)
    # print(request.data['name'])
    new_recipe.user = request.user
    rec = new_recipe.initial_data
    new_recipe.is_valid()
    print(new_recipe.errors)  # THIS LINE IS GOLD!!
    if new_recipe.is_valid():
        print("hi")
        try:
            new_recipe_saved = new_recipe.save()
        except Exception as e:
            raise e
    else:
        raise e
    return Response('Recipe saved', status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_recipes(request):
    recipes = Recipe.objects.all()
    serialized_data = RecipeSerializer(recipes, many=True).data
    return Response(serialized_data, status=status.HTTP_200_OK)

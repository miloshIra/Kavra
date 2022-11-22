from django.shortcuts import render, redirect

from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import RecipeSerializer, OrderSerializer, ReviewSerializer, TagSerializer
from .models import Recipe, Order, Review, Tag
from users.models import Profile
from django.core.exceptions import ValidationError

# Create your views here.

# .............. Recipes API .........................


@api_view(['POST'])
def create_recipe(request):
    """ Creates a new recipe ... at least it should .. if it works it's django magic."""

    profile = Profile.objects.get(user=request.user.id)
    new_recipe = RecipeSerializer(data=request.data)
    new_recipe.user = profile
    new_recipe.is_valid()
    print(new_recipe.errors)  # THIS LINE IS GOLD!!
    if new_recipe.is_valid():
        try:
            new_recipe_saved = new_recipe.save()
        except Exception as e:
            raise e

    serialized_data = RecipeSerializer(new_recipe_saved, many=False).data
    return Response(serialized_data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_recipe(request, pk):
    """ Updates a recipe ... at least it should .. if it works it's django magic."""
    print(pk)
    recipe = Recipe.objects.get(id=pk)
    updated_recipe = RecipeSerializer(recipe, data=request.data)  # LEARN THIS LINE!
    updated_recipe.is_valid()
    print(updated_recipe.errors)  # THIS LINE IS GOLD!!
    if updated_recipe.is_valid():
        try:
            updated_recipe_saved = updated_recipe.save()
        except Exception as e:
            raise e
    return Response('Recipe saved', status=status.HTTP_200_OK)


@api_view(['GET'])
def get_recipe_by_id(request, pk):
    recipes = Recipe.objects.get(id=pk)
    serialized_recipe = RecipeSerializer(recipes, many=False).data
    context = {'recipes': serialized_recipe}
    return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_recipes(request):
    recipes = Recipe.objects.all()
    serialized_data = RecipeSerializer(recipes, many=True).data
    context = {'recipes': serialized_data}
    return Response(context, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_recipe(request, pk):
    del_recipe = Recipe.objects.get(id=pk)
    del_recipe.delete()
    return Response("Recipe with id {} was deleted".format(pk))


# .............. Order API .........................

@api_view(['POST'])
def create_order(request):
    pass
    profile = Profile.objects.get(user_id=request.user.id)
    recipe = Recipe.objects.get(id=request.data['recipe']['id'])
    print(recipe)
    by_user = recipe.user.id
    new_order = OrderSerializer(data={**request.data, "for_user": profile.user.id,
                                                      "by_user": by_user,
                                                      "recipe": recipe.id})
    if new_order.is_valid():
        try:
            new_order_saved = new_order.save()
            print(new_order.errors)
        except Exception as e:
            raise e
    return Response(new_order.data)


@api_view(['PUT'])
def complete_order(request, pk):
    """ Updates a recipe ... at least it should .. if it works it's django magic."""
    print(pk)
    order = Order.objects.get(id=pk)
    order.completed = Order.Completed.yes
    updated_order = order
    try:
        updated_recipe_saved = updated_order.save()
    except Exception as e:
        raise e
    return Response('Order completed', status=status.HTTP_200_OK)


@api_view(['PUT'])
def cancel_order(request, pk):
    """ Updates a recipe ... at least it should .. if it works it's django magic."""
    print(pk)
    order = Order.objects.get(id=pk)
    order.completed = Order.Completed.canceled
    updated_order = order
    try:
        updated_recipe_saved = updated_order.save()
    except Exception as e:
        raise e
    return Response('Order canceled', status=status.HTTP_200_OK)


@api_view(['GET'])
def get_active_orders(request, pk):
    pass


@api_view(['GET'])
def get_all_orders(request):
    orders = Order.objects.all()
    serialized_data = OrderSerializer(orders, many=True).data
    context = {'orders': serialized_data}
    return Response(context, status=status.HTTP_200_OK)

# ................... TAGS api...................


@api_view(['POST'])
def create_tag(request):
    new_tag = TagSerializer(data=request.data)
    if new_tag.is_valid():
        tag_saved = new_tag.save()
    return Response("Tag saved", status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_tags(request):
    tags = Tag.objects.all()
    serialized_data = TagSerializer(tags, many=True).data
    context = {'tags': serialized_data}
    return Response(context, status=status.HTTP_200_OK)


# .......................... Review apis.........................

@api_view(['POST'])
def create_review(request):
    recipe = Recipe.objects.get(id=request.data['recipe'])
    new_review = Review(review=request.data['review'],
                        by_user=request.user.id,
                        owner=recipe)
    new_review.save()

    # print(new_review)
    # recipe.review = new_review
    # recipe.save()
    return Response("Review saved", status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_reviews(request):
    reviews = Review.objects.all()
    serialized_data = ReviewSerializer(reviews, many=True).data
    context = {'reviews': serialized_data}
    return Response(context, status=status.HTTP_200_OK)
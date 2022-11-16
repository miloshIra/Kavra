from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # CRUD for Recipes...
    path('recipes/', views.get_all_recipes, name="recipes"),
    path('recipes/<str:pk>', views.get_recipe_by_id, name="recipe"),
    path('recipes/create/', views.create_recipe, name="create_recipe"),
    path('recipes/delete/<str:pk>', views.delete_recipe, name="delete_recipe"),
    path('recipes/update/<str:pk>', views.update_recipe, name="update_recipes"),

]

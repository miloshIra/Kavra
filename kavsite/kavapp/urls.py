from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # CRUD for Recipes...
    path('recipes/', views.get_all_recipes, name="recipes"),
    path('recipes/<str:pk>', views.get_recipe_by_id, name="recipes"),
    path('recipes/create/', views.create_recipe, name="create_recipe"),
    path('recipes/delete/<str:pk>', views.delete_recipe, name="delete_recipe"),
    path('recipes/update/<str:pk>', views.update_recipe, name="update_recipes"),
    path('recipes/by_user/<str:pk>', views.get_recipe_by_user, name="get_recipes_by_user"),

    # CRUD for Orders...
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/', views.get_all_orders, name='orders'),
    path('orders/complete/<str:pk>', views.complete_order, name='complete_order'),
    path('orders/cancel/<str:pk>', views.cancel_order, name='cancel_order'),

    # Tags
    path('tags/', views.get_all_tags, name='tags'),
    path('tags/create/', views.create_tag, name="create_tag"),
    path('tags/add_to_recipe/', views.add_tag_to_recipe, name='add_tag'),

    # Reviews
    path('reviews/create/', views.create_review, name='create_review'),
    path('reviews/', views.get_all_reviews, name="reviews")

]

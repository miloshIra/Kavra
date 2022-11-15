from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # CRUD for Recipes...
    path('recipes/', views.get_all_recipes),
    path('recipes/create', views.create_recipe),
    path('recipes/<str:pk>', views.get_recipe_by_id),
    path('recipes/delete/<str:pk>', views.delete_recipe),
    path('recipes/update/<str:pk>', views.update_recipe),

]

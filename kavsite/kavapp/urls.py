from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.get_all_recipes),
    path('recipes/create', views.create_recipe),
    path('recipes/delete', views.delete_recipe_by_id),

]

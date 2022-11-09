from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('recipes/create', views.create_recipe),
    path('recipes/', views.get_all_recipes),
]

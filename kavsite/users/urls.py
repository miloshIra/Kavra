from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('create_user', views.create_user, name='create-user'),
    path('get_all_users', views.get_all_users, name='get_all_users')
]

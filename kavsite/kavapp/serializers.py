from dataclasses import field, fields
from rest_framework import serializers
from .models import Recipe, Review, HistoryLog, Order


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryLog
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


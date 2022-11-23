from dataclasses import field, fields
from rest_framework import serializers
from .models import Recipe, Review, Order, Tag


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class TagPrintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('recipe', 'created',)

from rest_framework import serializers
from API.views import *

class RestaurantSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cuisine = serializers.CharField(max_length=50)

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'cuisine', 'rating']

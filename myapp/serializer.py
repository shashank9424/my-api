from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer( serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
class GroupSerializer( serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class ProductSerializer( serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class CustomerSerializer( serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
class CitySerializer( serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
class StateSerializer( serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'
class CountrySerializer( serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
class TaxSerializer( serializers.ModelSerializer):
    class Meta:
        model = Tax
        fields = '__all__'
class Assessable_valueSerializer( serializers.ModelSerializer):
    class Meta:
        model = Assessable_value
        fields = '__all__'
class ItemSerializer( serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

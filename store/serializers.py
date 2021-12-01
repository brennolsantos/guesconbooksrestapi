from rest_framework import serializers
from .models import Book, Company, Magazine, Author, Basket, BasketItem, Promo, Genre

"""
This file use serializers in more generic way,
Cause the changes, updates and creations using the models
are very simple
"""


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class MagazineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine 
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author 
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre 
        fields = '__all__'

class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promo 
        fields = '__all__'

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket 
        fields = '__all__'

class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem 
        fields = '__all__'

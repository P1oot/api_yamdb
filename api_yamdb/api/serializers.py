from dataclasses import field
from rest_framework import serializers

from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category

    def validate(self, data):
        if data == {}:
            raise serializers.ValidationError(
                'Данные не корректны')
        return data


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    genre = GenreSerializer(many=True)
    class Meta:
        fields = ('name', 'year', 'description', 'category', 'genre')
        model = Title

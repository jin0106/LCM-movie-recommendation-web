from rest_framework import serializers
from .models import Movie
from .models import Genre


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    class GenreListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
    genres = GenreListSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class GenreListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
    genres = GenreListSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

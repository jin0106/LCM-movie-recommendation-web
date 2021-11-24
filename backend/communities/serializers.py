from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie, Genre
from django.contrib.auth import get_user_model


class ReviewListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username'),

    user = UserSerializer(read_only=True, required=False)

    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class GenreListSerializer(serializers.ModelSerializer):
            class Meta:
                model = Genre
                fields = '__all__'
        genres = GenreListSerializer(many=True)

        class Meta:
            model = Movie
            fields = '__all__'

    movie = MovieSerializer(read_only=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username'),

    user = UserSerializer(read_only=True, required=False)

    class Meta:
        model = Review
        fields = ('title', 'content',
                  'created_at', 'updated_at', 'movie', 'user', )

    def create(self, validated_data):
        return Review.objects.create(**validated_data)


class CommentSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(read_only=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username'),
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
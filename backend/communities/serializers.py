from rest_framework import serializers
from .models import Review, Comment
from movies.models import Movie
from django.contrib.auth import get_user_model


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title')

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('username'),

    user = UserSerializer(required=False)
    movie = MovieSerializer(required=False)

    class Meta:
        model = Review
        fields = ('title', 'content',
                  'created_at', 'updated_at', 'movie', 'user')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

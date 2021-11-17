from rest_framework import serializers
from .models import Review, Comment


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'title')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['is_private']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title','genres')

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Movie'
        fields = '__all__'
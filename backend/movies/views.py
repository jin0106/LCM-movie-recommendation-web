from django.shortcuts import get_object_or_404, render
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer, MovieListSerializer
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    movies = Movie.obejects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)
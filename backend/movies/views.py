from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response


# 전체 영화 목록 조회
@api_view(['GET'])
def movie_list(request):
    pass
    # movies = get_list_or_404(Movie)
    # serializers = MovieListSerializer(movies, many=True)
    # return Response(serializers.data)


# 특정 영화 목록 조회(pk값이 아닌 영화 이름으로 바꿀까 고민중)
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)


@api_view(['GET'])
def user_recommend(request):
    user = request.user
    genres = user.genre

    movies = get_list_or_404(Movie, genre=genres)
    print(movies)
    serializers = MovieSerializer(movies)
    return Response(serializers.data)

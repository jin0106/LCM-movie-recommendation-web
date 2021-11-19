from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from .models import Movie, Genre
from .serializers import GenreListSerializer, MovieSerializer, MovieListSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests


# 전체 영화 목록 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):

    movies = get_list_or_404(Movie)
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)


# 특정 영화 목록 조회(pk값이 아닌 영화 이름으로 바꿀까 고민중)
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_list_or_404(Movie, pk=movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def user_recommend(request):
    # 현재 위치 정보 받아오기 진행중
    # url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyDRNxAxFvZlpwHLb43bBc80UPnjh8J43I8'
    # data = {
    #     'considerIp': True,
    # }

    # result = requests.post(url, data)

    # print(result.text)

    user = request.user.genre.all()
    genres = []
    for i in user:
        i = str(i)[14:16]
        genres.append(int(i))
    movies = []
    for i in range(len(genres)):
        a = get_list_or_404(Movie, genres=genres[i])[:3]
        movies.extend(a)
    print(movies)
    # serializer = GenreListSerializer(a, many=True)
    # return Response(serializer.data)

# 장르에 대한 정보만 시리얼라이저 해서 넘겨주기
    # user = request.user
    # genre = get_list_or_404(Genre, user_genre=user.id)
    # serializer = GenreListSerializer(genre, many=True)
    # return Response(serializer.data)


def weather_recommend(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b1a32c0fd2033a695051df3761f95526'
    city = 'Daegu'
    # request the API data and convert the JSON to Python data types
    city_weather = requests.get(url.format(city)).json()
    # 필요한 정보들만 가져오기
    weather = {
        'city': city,
        'main': city_weather['weather'][0]['main'],
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    # 일단 딕셔너리로 날씨에 장르들 하나씩을 선택 하도록 함(더 좋은 방법 있으면 그걸로 구현)
    lst = {'clear sky': 28, 'few clouds': 12, 'overcast cloud': 16, 'drizzle': 35, 'rain': 80, 'shower rain': 99, 'thunderstorm': 18,
           'snow': 10751, 'mist': 14, 'broken clouds': 27, 'scattered clouds': 10749}
    genre = lst[weather['description']]
    # 장르와 같은 영화 정보들 가지고오기
    movies = Movie.objects.filter(genres=genre)[:10]

    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)

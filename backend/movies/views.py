from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from .models import Movie, Genre
from .serializers import GenreListSerializer, MovieSerializer, MovieListSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests
import json


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
def user_recommend(request):
    user = request.user.genre.all()
    genres = []
    for i in user:
        a = json.loads(json.dumps(str(i)))
        b = ''
        for j in str(a):
            if j.isdigit():
                b += j
        genres.append(b)


    input_serializer = []
    for i in range(len(genres)):
        a = Movie.objects.filter(genres=int(genres[i]))
        input_serializer.extend(a)
    
    serializer = MovieListSerializer(input_serializer, many=True)

    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['GET'])
def weather_recommend(request):
    # serializer.data,
    # 현재 위치 정보 받아오기 진행중
    LOCATION_API_KEY = 'AIzaSyB7Sx40393IyWF0OYSJ7OMUqY2dHCdxzsw'
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={LOCATION_API_KEY}'
    

    result = json.dumps(requests.post(url).json())
    location = json.loads(result)
    
    
    lat = location["location"]["lat"]
    lng = location["location"]["lng"]

    
    WEATHER_API_KEY = 'b1a32c0fd2033a695051df3761f95526'
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={WEATHER_API_KEY}'
    # request the API data and convert the JSON to Python data types
    city_weather = requests.get(url).json()
    # 필요한 정보들만 가져오기
    
    weather = {
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
    
    return Response(serializers.data, status.HTTP_200_OK)

from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework import response
from rest_framework.decorators import api_view, permission_classes

from communities.models import Review
from .models import Movie, Genre
from .serializers import GenreListSerializer, MovieSerializer, MovieListSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests
import json
import pprint
import urllib.request
from django.db.models import Avg
from config.settings import (
    CLIENT_ID,
    CLIENT_SECRET,
    TRANSLATE_NAVER_ID,
    TRANSLATE_NAVER_SECRET,
    LOCATION_API_KEY,
    WEATHER_API_KEY,
    YOUTUBE_API_KEY,
)
# 전체 영화 목록 조회


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializers = MovieListSerializer(movies, many=True)
    return Response(serializers.data)


# 특정 영화 목록 조회(pk값이 아닌 영화 이름으로 바꿀까 고민중)
@api_view(['GET'])
def get_score(request):
    movie =json.loads(request.GET['movie'])
    movie_pk = movie['id']
  
    movie = Movie.objects.get(pk=movie_pk)
    score = Review.objects.filter(movie=movie.id).values('score').aggregate(Avg('score'))
    if score['score__avg'] == None:
        score['score__avg'] = 0
    data = {
        'score' : round(score['score__avg'], 2)
    }
    return Response(data, status.HTTP_200_OK)


@api_view(['GET'])
def user_recommend(request):
    user_genres = request.user.genre.all()
    genres = []
    for user_genre in user_genres:
        genres.append(user_genre)
    input_serializer = []
    for id in genres:
        movie = Movie.objects.filter(genres=id).order_by("?")
        input_serializer.extend(movie)
    serializer = MovieListSerializer(input_serializer, many=True)
    return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
def weather_recommend(request):
    # serializer.data,
    # 현재 위치 정보 받아오기 진행중
    url = f'https://www.googleapis.com/geolocation/v1/geolocate?key={LOCATION_API_KEY}'

    result = json.dumps(requests.post(url).json())
    location = json.loads(result)

    lat = location["location"]["lat"]
    lng = location["location"]["lng"]

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
    if weather['description'] not in lst:
        genre = 28
    else:
        genre = lst[weather['description']]
    # 장르와 같은 영화 정보들 가지고오기

    movies = Movie.objects.filter(genres=genre).order_by("?")[:10]
    serializers = MovieListSerializer(movies, many=True)

    return Response(serializers.data, status.HTTP_200_OK)

# 장르별 영화 받아오기


@api_view(['GET'])
def genre_recommend(request):
    if request.method == 'GET':
        orderby = request.GET['orderby']
        # 정렬 분기점
        if orderby == 'title' or orderby == '-title':
            serializers = genre_orderby(request, orderby)
            return Response(serializers.data, status.HTTP_200_OK)
        elif orderby == 'release_date' or orderby == '-release_date':
            serializers = genre_orderby(request, orderby)
            return Response(serializers.data, status.HTTP_200_OK)
        elif orderby == 'popularity' or orderby == '-popularity':
            serializers = genre_orderby(request, orderby)
            return Response(serializers.data, status.HTTP_200_OK)
        elif orderby == 'vote_average' or orderby == '-vote_average':
            serializers = genre_orderby(request, orderby)
            return Response(serializers.data, status.HTTP_200_OK)
        elif orderby == 'random':
            genre_name = request.GET['genre']
            genre_number = Genre.objects.get(name=genre_name)
            movies = Movie.objects.filter(
                genres=genre_number).order_by("?")[:10]
            serializers = MovieListSerializer(movies, many=True)
            return Response(serializers.data, status.HTTP_200_OK)

# 장르별 정렬한 데이터 돌려줌


def genre_orderby(request, orderby):
    genre_name = request.GET['genre']
    genre_number = Genre.objects.get(name=genre_name)
    movies = Movie.objects.filter(genres=genre_number).order_by(orderby)
    serializers = MovieListSerializer(movies, many=True)
    return serializers


@api_view(['GET'])
def movie_search(request):

    # 네이버 영화정보 요청
    search_string = request.GET['search_string']

    url = f'https://openapi.naver.com/v1/search/movie.json?query={search_string}'
    header = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET,
    }
    res = requests.get(url, headers=header).json()
    english_title = []
    for movie in res['items']:
        english_title.append(movie['subtitle'])

    search_movies = []
    for title in english_title:
        try:
            movie = Movie.objects.filter(title=title).first()
            if movie == None:
                continue
            search_movies.append(movie)
        except Movie.DoesNotExist:
            continue

    # 해당 한글을 영어로 번역후 검색

    encText = urllib.parse.quote(search_string)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", TRANSLATE_NAVER_ID)
    request.add_header("X-Naver-Client-Secret", TRANSLATE_NAVER_SECRET)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode == 200):
        response_body = response.read()
        search_result = json.loads(response_body)[
            'message']['result']['translatedText']
        if search_result[-1] == '.':
            search_result = search_result[:len(search_result) - 1]
        word = search_result.split()
        if len(word) > 1:
            if word[0] == 'The':
                search_result = ''.join(word[1:])

        translate_movie = Movie.objects.filter(title__contains=search_result)
    else:
        print("Error Code:" + rescode)

    # 만약 네이버 api로도 검색 못하고 한글로도 검색 못했을 때 영어검색

    origin_movies = Movie.objects.filter(title__contains=search_string)

    search = len(search_movies)
    translate = len(translate_movie)
    origin = len(origin_movies)

    num = max(search, translate, origin)
    if num == search:
        movies = search_movies
    elif num == translate:
        movies = translate_movie
    else:
        movies = origin_movies

    serializers = MovieSerializer(movies, many=True)
    return Response(serializers.data, status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def movie_watched_list(request):

    if request.method == 'POST':
        user = get_user_model().objects.get(id=request.user.id)
        movie = Movie.objects.get(id=request.data['id'])
        if movie in user.watched_list.all():
            user.watched_list.remove(movie)
        else:
            user.watched_list.add(movie)
        user.save()
        return Response(status.HTTP_200_OK)

    else:
        movies = Movie.objects.filter(user_watched=request.user.id)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def movie_wish_list(request):

    if request.method == 'POST':
        user = get_user_model().objects.get(id=request.user.id)
        movie = Movie.objects.get(id=request.data['id'])
        if movie in user.wish_list.all():
            user.wish_list.remove(movie)
        else:
            user.wish_list.add(movie)
        user.save()
        return Response(status.HTTP_200_OK)

    else:
        movies = Movie.objects.filter(user_wish=request.user.id)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


# 해당 영화의 영상 주소 리턴
@api_view(['POST'])
def trailer(request):
    # 영화 객체 들어오면 영화 객체도 같이 넣어서 보내주기
    title = request.data['q']
    data = youtube(title)
    return Response(data, status.HTTP_200_OK)


# 홈페이지의 윗 쪽 영상들 랜덤 5개 리턴
@api_view(['GET'])
def main_movies(request):
    movies = list(Movie.objects.filter().order_by('-release_date'))
    movie0 = MovieSerializer(movies[8])
    movie1 = MovieSerializer(movies[1])
    movie2 = MovieSerializer(movies[2])
    movie3 = MovieSerializer(movies[3])
    movie4 = MovieSerializer(movies[9])

    data = {0: {'movie': movie0.data, 'src': 'https://www.youtube.com/embed/ZYzbalQ6Lg8?autoplay=1&mute=1&enablejsapi=1&controls=0&disablekb=1&modestbranding=1&rel=0&showinfo=0&start=6'},
            1: {'movie': movie1.data, 'src': 'https://www.youtube.com/embed/AxLH0lXEGAY?autoplay=1&mute=1&enablejsapi=1&controls=0&disablekb=1&modestbranding=1&rel=0&showinfo=0 '},
            2: {'movie': movie2.data, 'src': 'https://www.youtube.com/embed/drQWopZDEEY?autoplay=1&mute=1&enablejsapi=1&controls=0&disablekb=1&modestbranding=1&rel=0&showinfo=0 '},
            3: {'movie': movie3.data, 'src': 'https://www.youtube.com/embed/TLiI1wumchs?autoplay=1&mute=1&enablejsapi=1&controls=0&disablekb=1&modestbranding=1&rel=0&showinfo=0 '},
            4: {'movie': movie4.data, 'src': 'https://www.youtube.com/embed/9ix7TUGVYIo?autoplay=1&mute=1&enablejsapi=1&controls=0&disablekb=1&modestbranding=1&rel=0&showinfo=0 '}}
    return Response(data, status.HTTP_200_OK)


def youtube(title):
    params = {
        'key': YOUTUBE_API_KEY,
        'part': 'snippet',
        'q': title + ' official trailer',
        'type': 'video'
    }
    URL = "https://www.googleapis.com/youtube/v3/search"
    response = requests.get(URL, params=params)
    src = 'https://www.youtube.com/embed/' + \
        json.loads(response.text)['items'][0]['id']['videoId']
    data = {
        'src': src+'?autoplay=1&mute=0&enablejsapi=1&controls=0&disablekb=1&modestbranding=1&rel=0&showinfo=0'
    }
    return data


@api_view(['GET'])
def wish_list_recommend(request):
    id = request.user.id
    user = get_user_model().objects.get(id=id)
    wish_list = list(user.wish_list.all())
    watched_list = list(user.watched_list.all())
    if len(wish_list) > 1:
        genres_check = {}
        for movie in wish_list:
            genres = movie.genres.all()
            for genre in genres:
                if genre.name in genres_check:
                    genres_check[genre.name] += 1
                else:
                    genres_check[genre.name] = 1
        genres_check = sorted(genres_check.items())
        # 보고싶은 영화중 가장 많은 장르의 영화 추천
        genre_name = genres_check[0][0]
        genre_id = Genre.objects.get(name=genre_name)
        genre_id = genre_id.id

        movies = Movie.objects.filter(genres=genre_id).order_by("?")[:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    # 만약 wish 리스트가 비어 있다면 봣던 영화 목록 기준으로 돌려줌
    elif len(watched_list) > 1:
        genres_check = {}
        for movie in watched_list:
            genres = movie.genres.all()
            for genre in genres:
                if genre.name in genres_check:
                    genres_check[genre.name] += 1
                else:
                    genres_check[genre.name] = 1
        genres_check = sorted(genres_check.items())
        # 보고싶은 영화중 가장 많은 장르의 영화 추천
        genre_name = genres_check[0][0]
        genre_id = Genre.objects.get(name=genre_name)
        genre_id = genre_id.id

        movies = Movie.objects.filter(genres=genre_id).order_by("?")[:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    # 둘다 없다면 그냥 평점 기준으로 추천
    else:
        movies = Movie.objects.all().order_by('-vote_average')[:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


@api_view(['GET'])
def watched_list_recommend(request):
    id = request.user.id
    user = get_user_model().objects.get(id=id)
    watched_list = list(user.watched_list.all())
    if len(watched_list) > 1:
        genres_check = {}
        for movie in watched_list:
            genres = movie.genres.all()
            for genre in genres:
                if genre.name in genres_check:
                    genres_check[genre.name] += 1
                else:
                    genres_check[genre.name] = 1
        genres_check = sorted(genres_check.items())
        # 보고싶은 영화중 가장 많은 장르의 영화 추천
        genre_name = genres_check[0][0]
        genre_id = Genre.objects.get(name=genre_name)
        genre_id = genre_id.id

        movies = Movie.objects.filter(genres=genre_id).order_by("?")[:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    # 둘다 없다면 그냥 평점 기준으로 추천
    else:
        movies = Movie.objects.all().order_by('-vote_average')[:20]
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

#pp
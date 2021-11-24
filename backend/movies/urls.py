from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('', views.movie_list),
    path('get_score/', views.get_score),
    path('user_recommend/', views.user_recommend),
    path('weather_recommend/', views.weather_recommend),
    path('genre_recommend/', views.genre_recommend),
    path('movie_search/', views.movie_search),
    path('watched_movie/', views.movie_watched_list),
    path('wish_list/', views.movie_wish_list),
    path('trailer/', views.trailer),
    path('main_movies/', views.main_movies),
    path('wish_list_recommend/', views.wish_list_recommend),
    path('watched_recommend/', views.watched_list_recommend)
]

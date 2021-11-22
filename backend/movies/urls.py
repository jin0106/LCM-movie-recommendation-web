from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('user_recommend/', views.user_recommend),
    path('weather_recommend/', views.weather_recommend),
    path('genre_recommend/', views.genre_recommend),
    path('movie_search/', views.movie_search),
    path('watched_movie/', views.movie_watched_list),
    path('wish_list/', views.movie_wish_list),
]

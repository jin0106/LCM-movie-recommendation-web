from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

from movies.models import Genre
from movies.models import Movie

class User(AbstractUser):
    nickname = models.CharField(max_length=30, blank=True)
    genre = models.ManyToManyField(Genre, related_name="user_genre")
    profileimg = models.ImageField(blank=True)
    watched_list = models.ManyToManyField(Movie, related_name="user_watched", blank=True)
    wish_list = models.ManyToManyField(Movie, related_name="user_wish", blank=True)
    #followings = models.ManyToManyField('self', symmetrical=False, related_name='followers'),

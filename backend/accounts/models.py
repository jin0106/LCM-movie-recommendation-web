from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

from movies.models import Genre
from movies.models import Movie

class User(AbstractUser):
    pass
    #nickname = models.CharField(max_length=15),
    #genre = models.ManyToManyField(Genre, related_name="user_genre", null=True)
    #profileimg = models.ImageField(),
    #watched_list = models.ManyToManyField(Movie, related_name="user_watched", null=True),
    #wish_list = models.ManyToManyField(Movie, related_name="user_wish", null=True),
    #followings = models.ManyToManyField('self', symmetrical=False, related_name='followers'),

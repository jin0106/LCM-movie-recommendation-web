from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=15),
    #profileimg = models.ImageField(),
    #watched_list = models.ManyToManyField()
    #wish_list = models.ManyToManyField()
    #followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')

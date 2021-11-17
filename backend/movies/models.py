from django.db import models

# Create your models here.
<<<<<<< HEAD
=======
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_data = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField
>>>>>>> community

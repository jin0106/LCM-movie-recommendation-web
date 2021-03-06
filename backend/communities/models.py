from django.db import models
from movies.models import Movie
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review', blank=True)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(default=3, validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ], blank=True, null=True)
    """
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True)
  
    """
    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.CharField(max_length=100)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
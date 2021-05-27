# apx/models.py
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    interest = models.CharField(max_length=500)
    
    def __str__(self):
        return self.user.username

class userMovieWatched(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    movieNumber = models.IntegerField(primary_key = True)
    movieWatched = models.CharField(max_length=200)
    movieRating = models.IntegerField()

    def __str__(self):
        return self.user.username

class moviesData(models.Model):
    movieId = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=200)
    imdbID = models.IntegerField()
    year = models.IntegerField()
    rtPictureURL = models.URLField()

class moviesgenre(models.Model):
    movieId = models.IntegerField(primary_key = True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=800)
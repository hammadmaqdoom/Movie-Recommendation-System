# apx/admin.py

from django.contrib import admin
from apx.models import UserProfileInfo, User, userMovieWatched, moviesData, moviesgenre
# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(userMovieWatched)
admin.site.register(moviesData)
admin.site.register(moviesgenre)

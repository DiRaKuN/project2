from django.contrib import admin
from .models import Movie, MovieImage, Profile 

admin.site.register(Movie)
admin.site.register(MovieImage)
admin.site.register(Profile)
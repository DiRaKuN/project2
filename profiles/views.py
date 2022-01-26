from django.shortcuts import render
from .models import Movie

def movie_list(reqest):
	movies = Movie.objects.all()
	context = {
		'movies': movies	
	}
	return render(reqest, 'profiles/movie_list.html', context)
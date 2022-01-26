from django.db import models
from django.contrib.auth.models import User 


def movie_images_upload(instance, filename):
	return f'movie_{instance.movie.id}/{filename}'

def profile_image_upload(instance, filename): 
	return f'profiles/{instance.id}/{filename}'

class Profile(models.Model):
	profile_image = models.ImageField(upload_to=profile_image_upload)
	user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=60, null=True)
	phone_num = models.CharField(max_length=25, null=True)
	age = models.PositiveIntegerField()
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.name} {self.phone_num}'

	class Meta:
		ordering = ['-age']
		verbose_name = 'Профиль'
		verbose_name_plural = 'Профили'


class Movie(models.Model):
	name = models.CharField(max_length=60, verbose_name="Название фильма")
	description = models.TextField(verbose_name='Краткий сюжет')
	release_date = models.DateField(verbose_name='Дата выхода')

	def __str__(self):
		return f"{self.name} {self.release_date}"

	class Meta:
		verbose_name = "Фильм"
		verbose_name_plural = "Фильмы"


class  MovieImage(models.Model):
	file = models.ImageField(upload_to='movie_images')
	movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

	def __str__(self):
		return self.file.url

	class Meta:
		verbose_name ='Изображение к фильму'
		verbose_name_plural ='Изображение к фильму' 
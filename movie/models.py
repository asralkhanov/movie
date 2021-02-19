from django.db import models
from datetime import datetime
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import User

class Category(models.Model):
	name = models.CharField('Kategoriya nomi', max_length=50)
	slug = models.SlugField('*', unique=True, max_length=50)
	desc = models.TextField('Kategoriya haqida', blank=True, max_length=1500)

	def get_absolute_url(self):
		return reverse('movie:category_view', kwargs={'category_slug':self.slug})
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'



class Genre(models.Model):
	name = models.CharField('Janr nomi', max_length=50)
	slug = models.SlugField('*', unique=True, max_length=50)
	desc = models.TextField('Janr haqida', blank=True, max_length=500)



	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Janr'
		verbose_name_plural = 'Janrlar'


class Post(models.Model):
	title = models.CharField('Yangilik nomi', max_length=250)
	slug = models.SlugField('*',max_length=50, unique=True)
	desc = RichTextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
	published = models.DateTimeField('Qoshilgan vaqti', auto_now_add=True)
	author = models.CharField('Muallif', max_length=250, blank=True,null=True)
	views = models.PositiveIntegerField('Korildi', default=0)
	image = models.ImageField('Foto', upload_to='post_images/', null=True)

	class Meta:
		verbose_name = 'Yangilik'
		verbose_name_plural = 'Yangiliklar'
		
	def get_absolute_url(self):
		return reverse('movie:post_detail', kwargs={'post_slug':self.slug})

	def __str__(self):
		return self.title


	




class Actor(models.Model):
	name = models.CharField("Ismi", max_length=80)
	age = models.PositiveIntegerField("Yoshi", default=0)
	country = models.CharField('Millati', max_length=50, blank=True)
	date_brt = models.DateField('Tugilgan sanasi', )
	place_of_brt = models.CharField('Tugilgan joyi', max_length=90, blank=True)
	genres = models.ForeignKey(Genre, on_delete=models.CASCADE, blank=True, null=True)
	desc = RichTextField()
	image = models.ImageField('Foto', upload_to='actors_images')

	def get_absolute_url(self):
		return reverse('movie:actor_detail', kwargs={'slug':self.name})

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Aktyor'
		verbose_name_plural = 'Aktyorlar'

	

class Directors(models.Model):
	name = models.CharField('Ismi: ', max_length=80)
	age = models.PositiveIntegerField('Yoshi: ', default=0)
	country = models.CharField('Millati, Davlati: ', max_length=50)
	desc = models.TextField('Rejissor haqida: ', blank=True)
	movie = models.ForeignKey('Movie', on_delete=models.CASCADE,related_name='film_director', null=True)


	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Rejissor'
		verbose_name_plural = 'Rejissorlar'


class Movie(models.Model):
	title = models.CharField('Film nomi', max_length=250)
	slug = models.SlugField('*',max_length=50, unique=True)
	tagline = models.CharField('Film haqida qisqacha', max_length=500, default='', blank=False)
	desc = RichTextField()
	views = models.PositiveIntegerField('Korildi', default=0, blank=True , null=True)

	likes = models.ManyToManyField(User, blank=True,related_name='likes')
	trailer = RichTextField()

	slide_movie = models.BooleanField('Bosh sahifa sliderga',default=False)
	most_popular = models.BooleanField('Mashxur kinolar',default=False)
	home_poster = models.ImageField('Bosh sahifa posteri', upload_to='movie/', null=True,blank=True)
	poster = models.ImageField('Poster, default=182x268', upload_to='movie/')
	year = models.PositiveIntegerField('Chiqqan sanasi', default='2020')
	country = models.CharField('Davlat', max_length=30)
	actors = models.ManyToManyField(Actor, verbose_name='aktyorlar', related_name='film_actor')
	genres = models.ManyToManyField(Genre, verbose_name='Janrlar')
	world_premiere = models.DateField("Jahondagi premyera sanasi", default=datetime.today)
	budget = models.PositiveIntegerField("Byudjet", default=0, help_text="Ko'kida ko'rsatin")
	category = models.ForeignKey(Category, verbose_name='Kategoriya', on_delete=models.CASCADE, null=True)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Film'
		verbose_name_plural = 'Filmlar'

	def get_absolute_url(self):
		return reverse('movie:movie_detail', kwargs={'movie_slug':self.slug})

	def total_likes(self):
		return self.likes.count()





class Movie_Shots(models.Model):
	title = models.CharField('Nomi', max_length=150, blank=True, null=True)
	desc = models.TextField("Kadr haqida", blank=True, null=True)
	image = models.ImageField('Kadr', upload_to="movie_shots/")
	movie = models.ForeignKey(Movie, verbose_name='Film', on_delete=models.CASCADE, null=True, blank=True)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Kadr'
		verbose_name_plural = 'Kadrlar'


class RatingStar(models.Model):
	value = models.PositiveIntegerField("Qiymat", default=0)

	def __str__(self):
		return f'{self.value}'


	class Meta:
		verbose_name = 'Yulduz reytingi'
		verbose_name_plural = 'Yulduz reytinglari'
		ordering = ['-value']


class Rating(models.Model):
	ip = models.CharField('IP manzil', max_length=15, blank=True)
	star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='yulduz')
	movie = models.ForeignKey(Movie, on_delete=models.CharField, verbose_name='film')


	def __str__(self):
		return f"{self.star} - {self.movie}"


	class Meta:
		verbose_name = 'Reyting'
		verbose_name_plural = 'Reytinglar'


class Reviews(models.Model):
	name = models.CharField("Ism", max_length=60)
	email = models.EmailField('Email',)
	message = models.TextField('Xabar', blank=True)

	parent = models.ForeignKey(
		'self', verbose_name="parent", on_delete=models.SET_NULL , null=True, blank=True
		)

	movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_comments')
	
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Muhokama'
		verbose_name_plural = 'Muhokamalar'


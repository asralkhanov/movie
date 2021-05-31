from django.db import models

# Create your models here.

# *Category => name , slug
# *Genre => name,slug
# *Actors => name,slug,age,country,bio,films, image
# *Movie => title,slug,country,genre,year,budget, actors,producer,poster
# *Comment => name,message
# *Contact => fname,lname,email,subject,message

class Category(models.Model):
	name = models.CharField("Kategoriya nomi", max_length=150)
	slug = models.SlugField('*', max_length=100, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'


class Genre(models.Model):
	name = models.CharField("Janr nomi", max_length=150)
	slug = models.SlugField('*', max_length=100, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Janr'
		verbose_name_plural = 'Janrlar'

class Actors(models.Model):
	name = models.CharField('Ismi', max_length=150)
	slug = models.SlugField('*', max_length=100, unique=True)
	age = models.PositiveIntegerField('Yoshi', default=0, blank=True)
	country = models.CharField('Millati', max_length=100, blank=True)
	bio = models.TextField('Biografiya')
	image = models.ImageField('Rasmi', upload_to='actors/')
	# movies = models.ForeignKey(Movie, on_delete=models.PROTECT)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Aktyor'
		verbose_name_plural = 'Aktyorlar'


class Movie(models.Model):
	title = models.CharField('Kino nomi', max_length=250)
	slug = models.SlugField('*', max_length=100, unique=True)
	genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='genres')
	poster = models.ImageField('Poster', upload_to='movies/')
	director = models.CharField('Rejissor', max_length=100)
	actors = models.ForeignKey(Actors, on_delete=models.PROTECT, related_name='actors')
	country = models.CharField('Davlati', max_length=100, blank=True)
	year = models.PositiveIntegerField('Yili', default=2021)
	budget = models.PositiveIntegerField('Byudjet', default=0)


	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Kino'
		verbose_name_plural = 'Kinolar'




class Comment(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	name = models.CharField('Ism-Familya', max_length=100)
	message = models.TextField('Xabar')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Muhokama'
		verbose_name_plural = 'Muhokamalar'

class Contact(models.Model):
	first_name = models.CharField("Ism", max_length=30)
	last_name = models.CharField("Familya", max_length=30)
	email = models.EmailField('Email')
	subject = models.CharField('Mavzu', max_length=150)
	message = models.TextField('Xabar')

	def __str__(self):
		return self.first_name

	class Meta:
		verbose_name = 'Aloqa'
		verbose_name_plural = 'Aloqalar'

from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.


class HomePageView(View):
	# Home Page Movies View
	def get(self,request):
		movie = Movie.objects.all()
		return render(request, 'index.html', {'movies':movie})


class MovieDetailView(DetailView):
	# Movie Dewtail Page View
	model = Movie
	template_name = 'single.html'
	slug_field = 'slug'

class ContactPageView(View):
	# Contact page View
	def get(self, request):
		return render(request, 'contact.html')


# Test  views 

class AllPostView(ListView):
	model = Post
	paginated_by = 10
	template_name = 'news.html'
	context_object_name = 'posts'

class PostDetailView(DetailView):
	model = Post
	slug_field = 'slug'
	template_name = 'news-single.html'


def getCatPost(request,category_slug):
	category = PostCategory.objects.get(slug=category_slug)
	posts = category.posts.all
	return render(request, 'cat_post.html', {'posts':posts})

def getTagPost(request,tag_slug):
	tag = Tags.objects.get(slug=tag_slug)
	posts = tag.posts.all()
	return render(request, 'cat_post.html', {'posts':posts})



# Genres And Categories

def genreDetail(request, genre):
	genre = get_object_or_404(Genre, slug=genre)
	movie = Movie.objects.filter(genre=genre)
	context = {
		'movie':movie
	}
	return render(request, 'genres.html', context)


def search(request):
	q = request.GET.get('search', None)
	movies = Movie.objects.filter(title__icontains=q)
	posts = Post.objects.filter(title__icontains=q)
	total_results = len(movies) + len(posts)
	query = request.GET['search']
	context = {
		'movies':movies,
		'posts':posts,
		'total_results':total_results,
		'query':query
	}
	return render(request, 'searchResult.html', context)

# Errors 

def customHandler404(request, exception=None):
	return render(request, '404.html')
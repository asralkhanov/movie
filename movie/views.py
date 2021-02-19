from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView,DetailView
from django.views.generic.base import View

from django.http import JsonResponse

from .models import *
from contact.models import Contact
from django.shortcuts import get_object_or_404

from .forms import CommentForm, RatingForm
from django.db.models import Q
from django.core.paginator import Paginator


from contact.service import send
from contact.forms import ContactForm
# Create your views here.


class MoviesView(ListView):
	""" Movies View  class """
	model = Movie
	queryset = Movie.objects.all()# for movie in object_list
	template_name = 'movies/movie_list.html'

	movie = Movie.objects.all()




class MovieDetailView(View):
	""" Movie detail view class """
	def get(self, request, movie_slug):
		movie = get_object_or_404(Movie, slug=movie_slug)
		if movie.likes.filter(id=request.user.id).exists():
			is_liked = False
		else:
			is_liked = True
		# Counting movies
		movie.views += 1
		movie.save()
		last = Movie.objects.all().order_by('-id')[:8]
		return render(request, 'movies/single.html',{'movie':movie, 'lm':last,"is_liked":is_liked})




def like_movie(request):
	movie = get_object_or_404(Movie, id=request.GET.get('data'))
	if movie.likes.filter(id=request.user.id).exists():
		movie.likes.remove(request.user)
		is_liked = False
		status = "like"
	else:
		movie.likes.add(request.user)
		is_liked = True
		status = "dislike"
	context = {
	'status':status,
	'is_liked': is_liked,
	'total_likes': movie.total_likes()
	}
	# if request.is_ajax():
	#     html = render_to_string('movies/likes.html', context, request=request)
	return JsonResponse( context)


class CountLikes(View):
	#Counting likes
	def post(self, request, movie_id):
		movie = Movie.objects.get(id=movie_id)
		if request.method == 'POST':
			like = request.POST['like']
			print(like)
			if like == 1:
				movie.likes += 1
				movie.save()
			if like == 0:
				movie.dislikes += 1		
				movie.save()
		else:
			return  reverse('movie:movie_detail', kwargs={'movie_slug':movie.id})

		return  reverse('movie:movie_detail',kwargs={'movie_slug':movie.id})


class FilterMoviesView(ListView):
	#Filter Movies
	model = Movie
	template_name = 'movies/list.html'

	def get_queryset(self): # new 
		query = self.request.GET.get('q')
		object_list = Movie.objects.filter(
			Q(title__icontains=query) | Q(desc__icontains=query)
		)
		return object_list



class AddComment(View):
	""" Add Comments """
	def post(self,request,movie_id):
		print(request.POST)
		if request.method == 'POST':
			form = CommentForm(request.POST)
			if form.is_valid():
				c = form.save(commit=False)
				if request.POST.get("parent", None):
					form.parent_id = int(request.POST.get("parent"))
				m = get_object_or_404(Movie,id=movie_id)
				c.movie = m
				form.save()
				# Bu yerda komment qo'shilgani xaqida xabar shablonag jonatish kerak
				return HttpResponseRedirect(reverse("movie:movie_detail", kwargs = {"movie_slug":m.slug}))
		else:
			form = CommentForm()
			print('NO'*5)

		return render(request, 'movies/single.html',{'form':form} )


class ActorView(DetailView):
	""" Actors detail View"""
	model = Actor
	slug_field = 'name'
	template_name = 'movies/actor_detail.html'


class CategoryMoviesView(ListView):
	# Category Movies View
	def get(self, request, category_slug):
		category = Category.objects.get(slug=category_slug)
		movie = category.movie_set.all()

		paginator = Paginator(movie, 2) # Show 2 movies per page.
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)

		context = {'category_movie':movie, 'movies':page_obj}
		return render(request, 'movies/categories_list.html', context)


class AddRatingStar(View):
	""" Add Movie Rating """
	def get_client_ip(self, request):
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		return ip

	def post(self,request):
		form = RatingForm(request.POST)
		if form.is_valid():
			Rating.objects.update_or_create(
				ip=self.get_client_ip(request),
				movie_id=int(request.POST.get("movie")),
				defaults={'star_id':int(request.POST.get('star'))}
			)
			return HttpResponse(status=201)
		else:
			return HttpResponse(status=201)


class PostView(View):
	#Post List view
	def get(self,request):
		posts = Post.objects.all().order_by('-published')[:16]
		return render(request, 'movies/posts.html', {'posts':posts})


class PostDetailView(View):
	#Post detail view
	def get(self,request, post_slug):
		post = get_object_or_404(Post, slug=post_slug)
		return render(request, 'movies/post_detail.html', {'post':post})



def email_sender(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
		
			last_user = Contact.objects.all().order_by('-id')[:1]
			for email in last_user:
				if email:
					send(email)
			return render(request, 'movies/movie_list.html'	)

		
	else:
		form = ContactForm()
	return render(request, 'movies/movie_list.html', {'form':form})

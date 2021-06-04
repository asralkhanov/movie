from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView
from .models import *
# Create your views here.


class HomePageView(View):
	# Home Page Movies View
	def get(self,request):
		movie = Movie.objects.get(id=1)
		return render(request, 'index.html', {'movie':movie})


# Test  views 

class AllPostView(ListView):
	model = Post
	template_name = 'posts.html'



def getCatPost(request,category_slug):
	category = PostCategory.objects.get(slug=category_slug)

	print(category.__dir__())
	posts = category.categories.all()
	return render(request, 'cat_post.html', {'posts':posts})
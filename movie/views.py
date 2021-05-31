from django.shortcuts import render
from django.views.generic.base import View
from .models import *
# Create your views here.


class HomePageView(View):
	# Home Page Movies View
	def get(self,request):
		movie = Movie.objects.get(id=1)
		return render(request, 'index.html', {'movie':movie})
from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.


class HomePageView(View):
	# Home Page Movies View
	def get(self,request):
		return render(request, 'index.html')
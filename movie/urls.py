from django.urls import path 
from .import views

app_name = 'movie'

urlpatterns = [
	path('', views.HomePageView.as_view(), name='home'),

	#test url 
	path('posts/', views.AllPostView.as_view(), name='posts'),
	path('posts/<slug:category_slug>', views.getCatPost, name='category_posts')
]
from django.urls import path
from . import views


app_name = 'movie'

urlpatterns = [
    path('subscribe/', views.email_sender, name='subscribe'),


    path('', views.MoviesView.as_view(), name='movies_list'),
    path('<str:movie_slug>', views.MovieDetailView.as_view(), name='movie_detail'),
    path('news/', views.PostView.as_view(), name='posts'),
    path('news/<str:post_slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('add_comment/<int:movie_id>/', views.AddComment.as_view(), name='addcomment_view'),
    path('actor/<str:slug>', views.ActorView.as_view(), name='actor_detail'),
    path('results/', views.FilterMoviesView.as_view(), name='search_result'),
    path('add-rating/', views.AddRatingStar.as_view(), name='addrating'),
    path('likes/', views.like_movie, name='likes'),
    path('category/<str:category_slug>', views.CategoryMoviesView.as_view(), name='category_view'),


]
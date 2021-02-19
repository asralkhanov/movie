from django.urls import path
from .views import movie_contact
from . import views

app_name = 'contact'

urlpatterns = [
	path('contact/', views.movie_contact, name='contact'),
]
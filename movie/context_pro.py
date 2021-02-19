from .models import Category, Movie
from contact.forms import ContactForm,DefaultContactForm

def view_all(request):
	slide_movies = Movie.objects.all().order_by('-id')[:5]
	most_popular = Movie.objects.filter(most_popular=True)
	categories = Category.objects.all()

	subscribe_form = ContactForm()
	default_form = DefaultContactForm()

	context = {
		'subs_form':subscribe_form,
		'default_form':default_form,
		'slide_movies':slide_movies,
		'most_popular':most_popular,
		'categories':categories
	}
	return context
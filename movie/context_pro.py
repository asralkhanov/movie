from .models import *


def view_all(request):
	context = {
		'latest_post':Post.objects.all()[:5],
		'top_post':Post.objects.filter(top=True),

		'genres':Genre.objects.all(),
	}
	return context
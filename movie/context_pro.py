from .models import Post


def view_all(request):
	context = {
		'latest_post':Post.objects.all()[:5],
		'top_post':Post.objects.filter(top=True)
	}
	return context
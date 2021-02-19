from django.forms import ModelForm, Textarea
from django import forms 
from .models import Reviews, Rating , RatingStar
#ReCaptcha3


class CommentForm(ModelForm):
	#This form == models.Reviews to comments, movie

	#recaptcha3
	# captcha = ReCaptchaField()

	class Meta:
		model = Reviews
		fields = ('name','email', 'message',)
		widgets = {
			'message': Textarea(attrs={'cols': 30, 'rows': 8}),
		}
        

class RatingForm(ModelForm):
	
	star = forms.ModelChoiceField(
		queryset=RatingStar.objects.all(),widget=forms.RadioSelect(),empty_label=None
	)
	class Meta:
		model = Rating
		fields = ('star',)
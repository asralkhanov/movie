from django.shortcuts import render
from .models import DefaultContact
from .forms import DefaultContactForm

import telebot
TOKEN = '1208478917:AAHct4f4eDSWM_UIGtkr41mdI56LgousShs'
bot = telebot.TeleBot(TOKEN)

me =  668618297


def movie_contact(request):
	if request.method == 'POST':
		form = DefaultContactForm(request.POST)
		if form.is_valid():
			form.save()
		bot.send_message(me, 'Saytdan xabar bor!')    
	else:
		form = DefaultContactForm()
	return render(request, 'contact.html', {'form':form})

from .models import Contact, DefaultContact
from django import forms
from django.forms import Textarea

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('email',)

class DefaultContactForm(forms.ModelForm):
    class Meta:
        model = DefaultContact
        fields = ('f_name', 'l_name', 'email', 'subject','message', )
        widgets={
        'message':Textarea(attrs={'cols':30, 'rows':8})
        }
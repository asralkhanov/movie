from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        pass

class DefaultContact(models.Model):
	f_name = models.CharField('ism', max_length=100)
	l_name = models.CharField('familiya', max_length=100)
	email = models.EmailField('email', max_length=100)
	subject = models.CharField('mavzu', max_length=100)
	message = models.TextField('matn', max_length=100)

	def __str__(self):
		return f"Bizga murojat qilgan bor - {self.f_name}-{self.l_name}"

	class Meta():
		verbose_name='Aloqa'
		verbose_name_plural = 'Aloqalar'


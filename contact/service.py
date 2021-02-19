from django.core.mail import send_mail

def send(user_email):
    send_mail(
        'You have subscribed to our email Newsletter',
        'We will continiously send you spam',
        'jamolxonahmedov124@mail.ru',
        [user_email],
        fail_silently = False
    )

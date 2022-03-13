from django.shortcuts import render
from django.core.mail import send_mail
from port import settings
from django.contrib import messages
from .models import contact, port

# Create your views here.
def Home(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_email = request.POST['email']
        message = request.POST['msg']

        #send mail to me
        send_mail(
            f'PORTFOLIO WEBSITE - Contact Form Entry - {user_name}', #subject
            f'Message: \n \n {message} \n \n From: {user_email}', #message to be sent
            settings.EMAIL_HOST_USER, #from email
            ['theprotonguy@yahoo.com'], #to email
            fail_silently=True
        )

        #send email to user
        send_mail(
            'THE PROTON GUY - Contact Form Entry',
            f'Hello {user_name}. Thank you for visiting my website and contacting me. This is a verification email to confirm your request below: \n \n > {message}. \n \n I will be in touch with you shortly!',
            settings.EMAIL_HOST_USER,
            [user_email],
            fail_silently=True
        )

        #confirmation
        messages.success(request, 'Your request has been received! We will reply shortly...')

        #save to database
        new_contact = contact(name=user_name, email=user_email, message=message)
        new_contact.save()

        return render(request, 'portapp/index.html', {'name': user_name})

    file = port.objects.all()
    return render(request, 'portapp/index.html', {'file': file})
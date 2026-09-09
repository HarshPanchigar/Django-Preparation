from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse

# def send_test_email(request):
#     subject = 'Welcome to my blog'
#     message = "Thank you for subscribing MY BLOG"
#     from_email = "harshpanchigar@gmail.com"
#     recipient_list = ["harshpanchigar40@gmail.com"]

#     send_mail(subject,message,from_email,recipient_list)
#     return HttpResponse("test  email sent successfully!")

def send_test_email(request):
    subject = 'Welcome to my blog'
    message = render_to_string('email/welcome_email.html',{
        'username' : 'Harsh',
        'course' : 'Django Course'
    })
    email = EmailMessage(
        subject,
        message,
        "harshpanchigar@gmail.com",
        ["harshpanchigar40@gmail.com"]
    )
    email.content_subtype = 'html'
    email.send()
    return HttpResponse("test  email sent successfully!")

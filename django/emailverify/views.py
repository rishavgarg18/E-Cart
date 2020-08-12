from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

# Create your views here.
def sendmail(request):
    subject = "Click on the Link below to Verify Your Account"
    to = ['rishavag.edu@gmail.com']
    from_email = 'rgrgarg18@gmail.com'

    ctx = {
        'user': 'buddy',
        'purchase': 'Books'
    }

    message = get_template('email.html').render(ctx)
    msg = EmailMessage(subject, message, to=to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()

    return HttpResponse('email_two')
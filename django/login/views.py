from django.shortcuts import render
from .models import Users
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage

# Create your views here.
def login(request):
    if request.method=="POST":
        login_data=json.loads(request.body)
        email=login_data['email']
        password=login_data['password']
        if Users.objects.filter(email__contains=email,password__contains=password).filter(email=email,password=password).exists():
            status=list(Users.objects.filter(email__contains=email,password__contains=password).filter(email=email,password=password).values('status'))
            if status[0]['status']=='False':
    
                return JsonResponse('Please Verify Your Email To Continue',safe=False)
            else:
                return JsonResponse("OK",safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)

# def login_session_check(request):
#     if request.method=="GET":
#         if request.session.has_key('email'):
#             email = request.session['email']
#             return JsonResponse(email,safe=False)
#         else:
#             return JsonResponse('NO',safe=False)

def register(request):
    if request.method=="POST":
        login_data=json.loads(request.body)
        email=login_data['email']
        password=login_data['password']
        if Users.objects.filter(email__contains=email).filter(email=email).exists():
            return JsonResponse("Email Already Registered",safe=False)
        else:
            Users.objects.create(email=email,password=password,status='False')
            subject = "Click on the Link below to Verify Your Account"
            send_list=[]
            send_list.append(email)
            to = send_list
            from_email = 'rgrgarg18@gmail.com'

            ctx = {
                'user': email
            }

            message = get_template('email.html').render(ctx)
            msg = EmailMessage(subject, message, to=to, from_email=from_email)
            msg.content_subtype = 'html'
            msg.send()

            return JsonResponse('Mail Sent.Click on the verify link recieved on your email to Continue',safe=False)

def verifyemail(request,email):
    if request.method=="GET":
        Users.objects.filter(email=email).update(status=True)
        return HttpResponse("Email Has Been Verified Successfully")
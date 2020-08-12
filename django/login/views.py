from django.shortcuts import render
from .models import Users
from django.http import JsonResponse
import json

# Create your views here.
def login(request):
    if request.method=="POST":
        login_data=json.loads(request.body)
        email=login_data['email']
        password=login_data['password']
        if Users.objects.filter(email__contains=email,password__contains=password).filter(email=email,password=password).exists():
            sess=request.session['email'] = email
            print(sess)
            return JsonResponse('OK',safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)

def login_session_check(request):
    if request.method=="GET":
        if request.session.has_key('email'):
            email = request.session['email']
            return JsonResponse(email,safe=False)
        else:
            return JsonResponse('NO',safe=False)

from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
import json
import requests

def create_session(request):
    if request.method=="GET":
        
        request.session['name'] = 'username'
        request.session['password'] = 'password123'
        response= JsonResponse("COOKIE",safe=False)
    return response
    return response
def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')




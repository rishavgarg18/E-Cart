from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
import json
import requests
from random import randint
from .models import phone_verify


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
# Create your views here.
def sendsms(request):
    if request.method=="POST":
        data=json.loads(request.body)
        phone_no=str(data['phone_no'])
        url = "https://www.fast2sms.com/dev/bulk"
        otp=str(random_with_N_digits(5))

        payload ="sender_id=FSTSMS&message=Your%20OTP%20IS%20---%20"+otp+"&language=english&route=p&numbers="+phone_no
        headers = {
            'authorization': "ZY8LVdvA6XrReTf4DCitxa5PIGgBHnjomcpq0ObWhukswUM2FJmLpMSONa78IZDPozt2yfYQqTWd60nJ",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        response_data=response.json()
        print(response_data)
        if response_data['return']==True:
            auth_id=str(response_data['request_id'])
            save_data=phone_verify(phone_no=phone_no,otp=otp,auth_id=auth_id)
            save_data.save()
            return JsonResponse("OTP SEND SUCESSFULLY",safe=False)
        else:
            return JsonResponse("OTP NOT SEND",safe=False)

def verifysms(request):
    if request.method=="POST":
        data=json.loads(request.body)
        phone_no=data['phone_no']
        otp=data['otp']
        otp_check=phone_verify.objects.filter(phone_no=phone_no).values('otp').latest('datetime')
        print(otp_check)
        if otp_check['otp']==otp:
            return JsonResponse("Verified",safe=False)
        else:
            return JsonResponse("Wrong otp",safe=False)





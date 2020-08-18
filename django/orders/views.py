from django.shortcuts import render
from paytm import views
import json
from .models import orders
from products.models import Product
from django.http import JsonResponse
from paytmchecksum import PaytmChecksum
import requests
# Create your views here.
def ordersave(request):
    if request.method=="POST":
        data=json.loads(request.body)
        name=data['name']
        email=data['email']
        # data['productid']=int(data['productid'])

        address=data['address']
        pincode=data['pincode']
        phoneno=data['phoneno']
        productid=data['productid']
        orders.objects.create(name=name,email=email,address=address,pincode=pincode,productid_id=productid,phone_no=phoneno)
        price=Product.objects.filter(id=productid).values('price').latest('dateadded')
        orderid=orders.objects.filter(email=email).values('id').latest('date')
        orderid_id=orderid['id']
        orderid_id=str(orderid_id)
        amount=price['price']
        amount=str(amount)
        email=str(email)
        


        paytmParams = dict()

        paytmParams["body"] = {
            "requestType"   : "Payment",
            "mid"           : "MvhSMh12903239445983",
            "websiteName"   : "WEBSTAGING",
            "orderId"       : orderid_id,
            "callbackUrl"   : "https://merchant.com/callback",
            "txnAmount"     : {
                "value"     : amount,
                "currency"  : "INR",
            },
            "userInfo"      : {
                "custId"    : email,
            },
        }

        # Generate checksum by parameters we have in body
        # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
        checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "@neDJV6QZxIuTVBR")

        paytmParams["head"] = {
            "signature"	: checksum
        }

        post_data = json.dumps(paytmParams)

        # for Staging
        url = "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid=MvhSMh12903239445983&orderId="+orderid_id

        # for Production
        # url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"
        response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
        orders.objects.filter(id=orderid_id).update(checksumhash=response['head']['signature'],transtxn=response['body']['txnToken'])
        print(response['head']['signature'])
        print(response['body']['txnToken'])


# {'head': {'responseTimestamp': '1597728236722', 'version': 'v1', 'signature': 'Fmv/FEZUvqux9cWtr3O731UwauYgC8hgvRHGlJkaH+sTYC/FEk5Cp5156Tfy/x8wxaIejYXGsa3kEGyNuvrB6q5KegxuIr+03XA+R0eCAjc='}
# , 'body': {'resultInfo': {'resultStatus': 'S', 'resultCode': '0000', 'resultMsg': 'Success'}, 'txnToken': '59b61272e9f24436a243c9c837b5513f1597728236721', 'isPromoCodeValid': False, 'authenticated': False}}
def sendcodes(request):
    if request
        
        
       
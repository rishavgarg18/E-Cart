from django.shortcuts import render
from paytm import views
import json
from .models import orders
from products.models import Product
from django.http import JsonResponse,HttpResponse
from paytmchecksum import PaytmChecksum
import requests
from django.http import HttpResponse
from django.template import loader
import urllib.parse

# Create your views here.
def ordersave(request):
    if request.method=="POST":
        data=json.loads(request.body)
        name=data['name']
        email=data['email']
      

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
            "callbackUrl"   : "http://127.0.0.1:8000/orders/callback/",
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
        return_dict=dict()
      
        return_dict["orderid"]=orderid_id
        return JsonResponse(return_dict,safe=False)

def get_payment_page(request,orderid):
     if request.method=="GET":
         return_data=orders.objects.filter(id=orderid).values('id','transtxn').latest('date')
         ctx={
                'txnToken':return_data['transtxn'],
                'orderid':return_data['id']
            }
         return render(request,"payment.html",ctx)




# # {'head': {'responseTimestamp': '1597728236722', 'version': 'v1', 'signature': 'Fmv/FEZUvqux9cWtr3O731UwauYgC8hgvRHGlJkaH+sTYC/FEk5Cp5156Tfy/x8wxaIejYXGsa3kEGyNuvrB6q5KegxuIr+03XA+R0eCAjc='}
# # , 'body': {'resultInfo': {'resultStatus': 'S', 'resultCode': '0000', 'resultMsg': 'Success'}, 'txnToken': '59b61272e9f24436a243c9c837b5513f1597728236721', 'isPromoCodeValid': False, 'authenticated': False}}
# def sendcodes(request):
#     if request
def trans_status(environ):
    if environ.method=="POST":
        

        # initialize a dictionary
        paytmParams = dict()
        print(environ.body)
        print(type(environ.body))
        bytess=environ.body
        string=bytess.decode('ASCII')
        lists=string.split('&')
        orderid=lists[9]
        final_orderid1=orderid.split('=')
        final_orderid2=final_orderid1[1]

        print(final_orderid2)

         
        

        # body parameters
        paytmParams["body"] = {

            # Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
            "mid" : "MvhSMh12903239445983",

            # Enter your order id which needs to be check status for
            "orderId" : final_orderid2,}

        # Generate checksum by parameters we have in body
        # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
        checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "@neDJV6QZxIuTVBR")

        # head parameters
        paytmParams["head"] = {

            # put generated checksum value here
            "signature"	: checksum
        }

        # prepare JSON string for request
        post_data = json.dumps(paytmParams)

        # for Staging
        url = "https://securegw-stage.paytm.in/v3/order/status"

        # for Production
        # url = "https://securegw.paytm.in/v3/order/status"

        response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
        print(response)
        if response['body']['resultInfo']['resultCode']=='01':
            orders.objects.filter(id=final_orderid2).update(transiction_status="SUCCESS")
            return HttpResponse('Payment Successfull <br/> <a href="http://127.0.0.1/ecart/dashboard.html">Go to Home</a>')


                
            
from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
import json

# Create your views here.
def allproducts(request):
    if request.method=="GET":
        return_data=list(Product.objects.all().values())
        return JsonResponse(return_data,safe=False)

def viewproduct(request):
    if request.method=="POST":
         data=json.loads(request.body)
         id=data['productid']
         return_data=list(Product.objects.filter(id=id).values())
         return JsonResponse(return_data,safe=False)
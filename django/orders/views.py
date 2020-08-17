from django.shortcuts import render
from paytm import views
from .models import orders
from products.models import Product
# Create your views here.
def ordersave(request):
    if request.method=="POST":
        data=json.loads(request.body)
        name=data['name']
        # address=data['address']
        # pincode=data['pincode']
        # phone_no=data['phone_no']
        productid=data['productid']
        orders.objects.create(**data)
        price=Product.objects.filter(id=productid).values('price')
        orderid=orders.objects.filter(name=name).values('id').latest('date')
        orderid_id=orderid['id']
        amount=price['price']
        initiate(orderid_id,amount,name)



        
        
       
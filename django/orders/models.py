from django.db import models
from products.models import Product
# Create your models here.
class orders(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    pincode=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=20)
    productid=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    checksumhash=models.CharField(max_length=1000)
    transtxn=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)
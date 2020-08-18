from django.db import models

# Create your models her
class Product(models.Model):
    category=models.CharField(max_length=50)
    name=models.CharField(max_length=500)
    price=models.CharField(max_length=10)
    description=models.CharField(max_length=1000)
    image=models.CharField(max_length=1000)
    dateadded=models.DateTimeField(auto_now_add=True)


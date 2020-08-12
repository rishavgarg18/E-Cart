from django.db import models

# Create your models here.
class phone_verify(models.Model):
    phone_no=models.CharField(max_length=50)
    otp=models.CharField(max_length=50)
    auth_id=models.CharField(max_length=500)
    datetime=models.DateTimeField(auto_now_add=True)

from .views import sendmail
from django.urls import path

urlpatterns = [  
 
    path('sendmail/', sendmail),
   
]
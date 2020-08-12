from .views import sendsms,verifysms
from django.urls import path

urlpatterns = [  
 
    path('sendsms/', sendsms),
    path('verifysms/', verifysms),
]
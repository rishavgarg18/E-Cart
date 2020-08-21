from .views import ordersave,get_payment_page,trans_status
from django.urls import path

urlpatterns = [  
 
    path('new/', ordersave),
    path('showpaymentpage/<int:orderid>/', get_payment_page),
    path('callback/',trans_status ),
]
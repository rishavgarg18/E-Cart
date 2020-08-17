from .views import ordersave
from django.urls import path

urlpatterns = [  
 
    path('new/', ordersave),
]
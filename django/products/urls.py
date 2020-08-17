from .views import allproducts,viewproduct
from django.urls import path

urlpatterns = [
    
    path('all/',allproducts),
    path('all/viewproduct/',viewproduct),
 

]
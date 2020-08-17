from .views import login,register,verifyemail
from django.urls import path

urlpatterns = [
    
    path('',login),
    path('new/',register),
    path('new/<str:email>/',verifyemail),
    

]
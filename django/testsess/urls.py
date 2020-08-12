from .views import create_session,access_session
from django.urls import path

urlpatterns = [  
 path('create/', create_session),
    path('access', access_session),
   
]
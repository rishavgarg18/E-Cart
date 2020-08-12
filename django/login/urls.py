from .views import login,login_session_check
from django.urls import path

urlpatterns = [
    
    path('',login_session_check),
    path('new/',login),

]
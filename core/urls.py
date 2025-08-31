from django.urls import path
from .views import whatsapp_redirect

urlpatterns = [
    path('chat/', whatsapp_redirect, name='whatsapp_redirect'),
]

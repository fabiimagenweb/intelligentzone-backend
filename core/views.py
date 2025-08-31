from django.shortcuts import render
from django.shortcuts import redirect

def whatsapp_redirect(request):
    return redirect("https://wa.me/573118052361")  # Número oculto

# Create your views here.

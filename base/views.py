from django.shortcuts import render,redirect
from .models import Donation

def home(request):
    return render(request, 'index.html')
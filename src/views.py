from django.shortcuts import render, HttpResponse
from .logic_ import age

def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def logic(request):
    return render(request, "login.html", {"terms": age})
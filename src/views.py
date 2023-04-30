from django.shortcuts import render, HttpResponse
import loginlogic

def home(request):
    return HttpResponse(request, "home.html")

def login(request):
    return render(request, "login.html")

def logiclogin(request):
    age = loginlogic.age
    return render(request, "login.html", age)

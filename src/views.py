from django.shortcuts import render, HttpResponse

def main(request):
    return HttpResponse("<h1>In development</h1>")

def login(request):
    return render(request, "login.html")
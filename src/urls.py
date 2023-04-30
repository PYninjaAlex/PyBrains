from django.urls import path
from .views import *

urlpatterns = [
    path('home', home),
    path('', login),
    path('logic', logic)
]
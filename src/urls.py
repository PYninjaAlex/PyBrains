from django.urls import path
from .views import *
from loginlogic import *

urlpatterns = [
    path('login', login),
    path('', home, name='home')
]
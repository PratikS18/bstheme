from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('tables.html', tables, name='tables'),
    path('login.html', sign_in, name='sign_in'),
    path('logout.html', sign_out, name='sign_out'),
    path('register.html', register, name='register'),
    path('<str:isbn1>', display_prod, name="display_prod"),
]

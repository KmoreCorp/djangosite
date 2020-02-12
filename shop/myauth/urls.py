from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myauth'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.mylogin, name='login'),
    path('logout/', views.mylogout, name='logout'),
    path('register/', views.register, name='register'),
]

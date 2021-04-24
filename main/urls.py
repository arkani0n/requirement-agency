from django.contrib import admin
from django.urls import path, include
from .views import render_main_page

urlpatterns = [
    path('',render_main_page,name='main_page')
    ]
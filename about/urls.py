
from django.contrib import admin
from django.urls import path, include
from .views import AboutView, LogoView

urlpatterns = [
       path('', AboutView.as_view()),
       path('logo', LogoView.as_view()),

       
]
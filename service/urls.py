
from django.contrib import admin
from django.urls import path, include
from .views import ServiceView, ServiceDetailsView

urlpatterns = [
       path('', ServiceView.as_view()),
       path('<int:pk>', ServiceDetailsView.as_view())
]
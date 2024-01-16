
from django.contrib import admin
from django.urls import path, include
from .views import BlogView, BlogDetailsView

urlpatterns = [
       path('', BlogView.as_view()),
       path('<int:pk>', BlogDetailsView.as_view())
]
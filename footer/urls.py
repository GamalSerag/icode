from django.urls import path
from .views import Footerview
urlpatterns = [
       path('', Footerview.as_view()),
              
]
from django.urls import path
from .views import HomeContent

urlpatterns = [
    path('', HomeContent.as_view(), name='home-content'),
]
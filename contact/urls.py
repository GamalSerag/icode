
from django.urls import path
from .views import ContactMessageCreateView, ContactView

urlpatterns = [
   
    path('social-links/', ContactView.as_view()),
    path('messages/', ContactMessageCreateView.as_view()),


]
from django.shortcuts import render
from rest_framework import generics
from .serializers import FooterSerializer
from .models import Footer

class Footerview(generics.ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
   
    serializer = serializer_class(queryset, many=True)
from django.shortcuts import render
from rest_framework import generics
from .serializers import AboutSerializer
from .models import About
from rest_framework.response import Response




class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = {'description': serializer.data[0]['description']}

        return Response(response_data)

class LogoView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = {
            'logo1': serializer.data[0]['logo1'],
            'logo2': serializer.data[0]['logo2'],
        }
        return Response(response_data)

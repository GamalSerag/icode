from django.shortcuts import render
from rest_framework import generics
from .serializers import ContactMessageSerializer, ContactSerializer
from .models import ContactMessage, Contacts
from rest_framework.response import Response


class ContactView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

       
        serialized_data = [{'whatsapp':item['whatsapp'], 'facebook': item['facebook'], 'instagram': item['instagram'], 'linkedin': item['linkedin']} for item in serializer.data]
       

        return Response(serialized_data)
    

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        # Call the super create method to perform the actual creation logic
        response = super().create(request, *args, **kwargs)

        # Customize the response to only include the status code
        return Response({"status": response.status_code}, status=response.status_code)
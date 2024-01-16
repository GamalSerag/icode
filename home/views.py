# combined/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Blog
from service.models import Service
from blog.serializers import BlogSerializer
from service.serializers import ServiceSerializer

# combined/views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Blog
from service.models import Service
from blog.serializers import BlogSerializer
from service.serializers import ServiceSerializer
from .models import Partners
from .serializers import PartnerSerializer

class HomeContent(APIView):
    def get(self, request, *args, **kwargs):
        language = request.headers.get('accept-language', 'en')

        blogs_queryset = Blog.objects.all()[:3]
        blogs_serializer = BlogSerializer(blogs_queryset, many=True, context={'request': request})

        # Get the first 3 services
        services_queryset = Service.objects.all()[:3]
        services_serializer = ServiceSerializer(services_queryset, many=True, context={'request': request})

        partners_queryset = Partners.objects.all()
        partners_serializer = PartnerSerializer(partners_queryset,  many=True, context={'request': request})
        # Select fields based on the language
        if language == 'en':
            combined_data = {
                'blogs': [{'id':blog['id'], 'title': blog['title'], 'description': blog['description'], 'image': blog['image']} for blog in blogs_serializer.data],
                'services': [{'id':service['id'], 'title': service['title'], 'description': service['description'], 'image': service['image']} for service in services_serializer.data],
                'partners': [{'id': partner['id'],'name':partner['partner_name'], 'image': partner['image']} for partner in partners_serializer.data]
            
            }   
        elif language == 'ar':
            combined_data = {
                'blogs': [{'id':blog['id'], 'title': blog['title_ar'], 'description': blog['description_ar'], 'image': blog['image']} for blog in blogs_serializer.data],
                'services': [{'id':service['id'], 'title': service['title_ar'], 'description': service['description_ar'], 'image': service['image']} for service in services_serializer.data],
                'partners': [{'id': partner['id'],'name':partner['partner_name'], 'image': partner['image']} for partner in partners_serializer.data]
            }
        else:
            # If the language is not 'en' or 'ar', you can define a default behavior here.
            combined_data = {
                'blogs': [{'id':blog['id'], 'title': blog['title'], 'description': blog['description'], 'image': blog['image']} for blog in blogs_serializer.data],
                'services': [{'id':service['id'], 'title': service['title'], 'description': service['description'], 'image': service['image']} for service in services_serializer.data],
                'partners': [{'id': partner['id'],'name':partner['partner_name'], 'image': partner['image']} for partner in partners_serializer.data]
            }

        return Response(combined_data)


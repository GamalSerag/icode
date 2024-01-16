from rest_framework.response import Response
from rest_framework import generics
from .serializers import BlogSerializer
from .models import Blog


from django.urls import reverse

class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def list(self, request, *args, **kwargs):
        language = request.headers.get('accept-language', 'en')
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        if language == 'en':
            serialized_data = [{'id': item['id'], 'title': item['title'], 'description': item['description'], 'image': item['image']} for item in serializer.data]
        elif language == 'ar':
            serialized_data = [{'id': item['id'], 'title': item['title_ar'], 'description': item['description_ar'], 'image': item['image']} for item in serializer.data]
        else:
            serialized_data = [{'id': item['id'], 'title': item['title'], 'description': item['description'], 'image': item['image']}for item in serializer.data]

        return Response(serialized_data)

    





from django.urls import reverse

class BlogDetailsView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        language = request.headers.get('accept-language', 'en')
        serializer = self.get_serializer(instance)

        if language == 'en':
            serialized_data = {'id': serializer.data['id'], 'title': serializer.data['title'], 'description': serializer.data['description'], 'image': serializer.data['image']}
        elif language == 'ar':
            serialized_data = {'id': serializer.data['id'], 'title': serializer.data['title_ar'], 'description': serializer.data['description_ar'], 'image': serializer.data['image']}
        else:
            serialized_data = {'id': serializer.data['id'], 'title': serializer.data['title'], 'description': serializer.data['description'], 'image': serializer.data['image']}

        # Convert the absolute image URL to a relative path

        return Response(serialized_data)



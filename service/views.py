from rest_framework.response import Response
from rest_framework import generics
from .serializers import ServiceSerializer
from service.models import Service


# class ServiceView(generics.ListAPIView):

#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     serializer = serializer_class(queryset, many=True)


# class ServiceDetailsView(generics.RetrieveAPIView):

#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     serializer = serializer_class(queryset, many=True)


class ServiceView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def list(self, request, *args, **kwargs):
        language = request.headers.get('accept-language', 'en')
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        if language == 'en':
            serialized_data = [{'title': item['title'], 'description': item['description'], 'image': item['image']} for item in serializer.data]
        elif language == 'ar':
            serialized_data = [{'title': item['title_ar'], 'description': item['description_ar'], 'image': item['image']} for item in serializer.data]
        else:
            serialized_data = [{'title': item['title_en'], 'description': item['description_en'], 'image': item['image']} for item in serializer.data]

        return Response(serialized_data)

class ServiceDetailsView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        language = request.headers.get('accept-language', 'en')

        serializer = self.get_serializer(instance)

        if language == 'en':
            serialized_data = {'title': serializer.data['title'], 'description': serializer.data['description'], 'image': serializer.data['image']}
        elif language == 'ar':
            serialized_data = {'title': serializer.data['title_ar'], 'description': serializer.data['description_ar'], 'image': serializer.data['image']}
        else:
            serialized_data = {'title': serializer.data['title'], 'description': serializer.data['description'], 'image': serializer.data['image']}

        return Response(serialized_data)
    




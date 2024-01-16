from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import LandingPage
from .serializers import LandingPageSerializer

@api_view(['GET'])
def landing_view(request):
    

    queryset = LandingPage.objects.all()
    serializer_class = LandingPageSerializer
    serializer = serializer_class(queryset, many=True, context={'request': request})

    language = request.headers['Accept-Language']
    if language == 'en':

        serialized_data = [{'id':item['id'],'title': item['title_en'], 'description' :item['description_en'], 'image': item['image'] } for item in serializer.data]
    elif language == 'ar':

        serialized_data = [{'id':item['id'],'title': item['title_ar'], 'description': item['description_ar'], 'image': item['image']} for item in serializer.data]


    return Response(serialized_data)





    

    



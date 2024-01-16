from rest_framework import serializers
from .models import Partners

class PartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Partners
        fields = '__all__'
from rest_framework.serializers import ModelSerializer
from .models import *


class HotelImagesSerializer(ModelSerializer):
    class Meta:
        model=HotelImages
        fields='__all__'

        
    
class HotelSerializer(ModelSerializer):
    H_photos=HotelImagesSerializer(many=True, read_only=True)
    class Meta:
        model = Hotel
        fields = '__all__'




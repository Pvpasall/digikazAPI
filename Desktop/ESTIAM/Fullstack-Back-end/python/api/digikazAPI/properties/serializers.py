from rest_framework import serializers
from .models import PropertiesModel


class PropertiesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PropertiesModel
        fields = ['id','title', 'description', 'userId', 'location', 'price', 'property_type', 'size']  



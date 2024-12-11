from rest_framework import serializers
from .models import FAQ


class FAQListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
    
class FAQRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

class FAQWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
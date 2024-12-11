from rest_framework import serializers
from .models import OurService

class SreviceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = '__all__'

class SreviceRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = '__all__'


class SreviceWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = '__all__' 
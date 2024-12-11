from rest_framework import serializers
from .models import Banner

class BannerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class BannerRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class BannerReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
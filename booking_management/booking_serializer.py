from rest_framework import serializers
from .models import BookingManagement

class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingManagement
        fields = '__all__'

class BookingRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingManagement
        fields = '__all__'

class BookingWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingManagement
        fields = '__all__'
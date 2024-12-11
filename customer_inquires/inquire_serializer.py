from rest_framework import serializers
from .models import CustomerInquiry

class InquireListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInquiry
        fields = '__all__'

class InquireRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInquiry
        fields = '__all__'

class InquireWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInquiry
        fields = '__all__'
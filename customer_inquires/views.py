from django.shortcuts import render
from .models import CustomerInquiry
from .inquire_serializer import InquireListSerializer, InquireRetriveSerializer, InquireWriteSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers


# Create your views here.
class CustomerInquireViewSet(ModelViewSet):
    queryset = CustomerInquiry.objects.all()
    # serializer_class = InquireSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return InquireListSerializer
        elif self.action == 'retrive':
            return InquireRetriveSerializer
        else:
            return InquireWriteSerializer
    

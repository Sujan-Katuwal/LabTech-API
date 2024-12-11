from django.shortcuts import render
from .models import BookingManagement
from .booking_serializer import BookingListSerializer, BookingRetriveSerializer, BookingWriteSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers


# Create your views here.
class BookingViewSet(ModelViewSet):
    queryset = BookingManagement.objects.all()
    # serializer_class = BookingSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return BookingListSerializer
        elif self.action == 'retrieve':
            return BookingRetriveSerializer
        else:
            return BookingWriteSerializer

            
    

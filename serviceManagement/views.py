from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import OurService
from .service_serializer import SreviceListSerializer, SreviceRetriveSerializer, SreviceWriteSerializer

# Create your views here.
class ServiceViewSet(ModelViewSet):
    queryset = OurService.objects.all()
    # serializer_class = SreviceSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return SreviceListSerializer
        elif self.action == 'retrive':
            return SreviceRetriveSerializer
        else:
            return SreviceWriteSerializer
    

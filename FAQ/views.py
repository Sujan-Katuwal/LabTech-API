from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import FAQ
from .faq_serializer import FAQListSerializer, FAQRetriveSerializer, FAQWriteSerializer 

# Create your views here.
class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    def get_serializer_class(self):
        if self.action == 'list':
            return FAQListSerializer
        elif self.action == 'retrieve':
            return FAQRetriveSerializer
        else:
            return FAQWriteSerializer

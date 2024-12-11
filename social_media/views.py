from django.shortcuts import render
from .models import SocialMedia
from .social_media_serializer import SocialMediaListSerializer, SocialMediaRetriveSerializer, SocialMediaWriteSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .social_media_permission import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .social_media_filter import SocalMediaFilter


# Create your views here.
class SocialMediaViewSet(ModelViewSet):
    queryset = SocialMedia.objects.all()
    # serializer_class = SocialMediaerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return SocialMediaListSerializer
        elif self.action == 'retrieve':
            return SocialMediaRetriveSerializer
        else:
            return SocialMediaWriteSerializer
        
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    #allows filtering based on query parameters
    filter_backends = [DjangoFilterBackend] 
    filterset_class = SocalMediaFilter
    

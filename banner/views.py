from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Banner
from .banner_serializer import BannerListSerializer, BannerRetriveSerializer, BannerReadSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .banner_permission import IsAdminOrReadOnly


# Create your views here.
class BannerViewSet(ModelViewSet):
    queryset = Banner.objects.all()
    # serializer_class = BannerSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return BannerListSerializer
        elif self.action == 'retrive':
            return BannerRetriveSerializer
        else:
            return BannerReadSerializer
    
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
        
    
    def create(self, request, *args, **kwargs):
        banner_exist = Banner.objects.first()

        if banner_exist:
            serializer = BannerReadSerializer(banner_exist, data = request.data, partial =True)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Banner updated !!!!"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import CustomUser
from .account_serializer import UserListSerializer, UserRetriveSerializer, UserWriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from .account_permission import IsAdminOrReadOnly


# Create your views here.
class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    # serializer_class = UserSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        elif self.action == 'retrieve':
            return UserRetriveSerializer
        else:
            return UserWriteSerializer
    
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]








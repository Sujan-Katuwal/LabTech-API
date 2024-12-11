from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .branch_serializer import BranchListSerializer, BranchRetriveSerializer, BranchWriteSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Branch


# Create your views here.
class BranchViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    # serializer_class = BranchSerializer
    def get_serializer_class(self):
        if self.action == 'list':
            return BranchListSerializer
        elif self.action == 'retrive':
            return BranchRetriveSerializer
        else:
            return BranchWriteSerializer


 





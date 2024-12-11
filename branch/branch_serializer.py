from rest_framework import serializers
from .models import Branch

class BranchListSerializer(serializers.ModelSerializer):

     class Meta:
        model = Branch
        fields = ['branch_name', 'email', 'phone_no', 'location', 'gps_location', 'branch_type']

class BranchRetriveSerializer(serializers.ModelSerializer):

     class Meta:
        model = Branch
        fields = ['branch_name', 'email', 'phone_no', 'location', 'gps_location', 'branch_type']

class BranchWriteSerializer(serializers.ModelSerializer):

     class Meta:
        model = Branch
        fields = ['branch_name', 'email', 'phone_no', 'location', 'gps_location', 'branch_type']
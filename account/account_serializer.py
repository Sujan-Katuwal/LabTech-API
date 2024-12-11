from rest_framework import serializers
from .models import CustomUser

class UserListSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'phone', 'role', 'gender']
        
class UserRetriveSerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'email', 'password', 'phone', 'role', 'gender']
        
class UserWriteSerializer (serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'email', 'password', 'phone', 'role', 'gender']


    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            role=validated_data['role'],
            gender=validated_data.get('gender', '')
        )
        return user
        

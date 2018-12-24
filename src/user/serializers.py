from rest_framework import serializers

from .models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'name', 'password',
        )
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email', 'name',
        )

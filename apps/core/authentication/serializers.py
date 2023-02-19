from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import Group


class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True, write_only=True)
    contact = serializers.CharField(required=True)
    full_name = serializers.CharField(required=True)
    is_customer = serializers.BooleanField(write_only=True)
    is_staff = serializers.BooleanField(write_only=True)


    class Meta:
        model = UserProfile
        fields = ('id', 'full_name', 'password', 'username', 'email', 'contact', 'is_customer', 'is_staff')


    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = UserProfile(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user

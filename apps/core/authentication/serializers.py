from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import Group


class UserProfileSerializer(serializers.ModelSerializer):
    # custom_groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all(), related_name='custom_user_groups')

    class Meta:
        model = UserProfile
        fields = ('id', 'full_name', 'username', 'email', 'contact', 'is_customer')

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import UserProfile
from .serializers import UserProfileSerializer


class ListCreateUserList(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class RetrieveUpdateDestroyUserDetail(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
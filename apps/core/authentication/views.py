from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import UserProfile
from .serializers import UserProfileSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

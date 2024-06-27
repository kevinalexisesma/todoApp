from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import ProfileCreationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

class ProfileCreationView(generics.CreateAPIView):
    
    queryset = get_user_model(). objects.all()
    serializer_class = ProfileCreationSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        return self.request.user.tasks.all()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


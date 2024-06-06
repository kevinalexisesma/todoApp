from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Profile
<<<<<<< Updated upstream

class ProfileCrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'emil', 'bio']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(ProfileCrationSerializer, self).create(validated_data)
=======
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.validators import RegexValidator


class ProfileCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'email', 'bio']
    
    def create(self, validated_data) :
        
        return super(ProfileCreationSerializer, self). create(validated_data)
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
     def validate(self, attrs):
        data = super().validate(attrs)

        # Añadir claims personalizados
        data['username'] = self.user.username

        return data
>>>>>>> Stashed changes

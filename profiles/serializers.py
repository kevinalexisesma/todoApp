from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class ProfileCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','username', 'password', 'email', 'bio']

    def create(self, validated_data) : 
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(ProfileCreationSerializer, self). create(validated_data)
    
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password], 
        error_messages={
            'required': 'La contraseña es obligatoria.',
        }
    )
   
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
        
    def validate(self, attrs):
            data = super().validate(attrs)

            # Añadir claims personalizados
            data['username'] = self.user.username
            return data
        
    def create(self, validated_data):
            return super(ProfileCreationSerializer, self).create(validated_data)

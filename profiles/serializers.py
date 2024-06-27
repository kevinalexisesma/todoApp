from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.validators import RegexValidator


class ProfileCreationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[
        RegexValidator(
            regex=r'^(?=.*[A-Z])',  # Al menos una letra mayúscula
            message=('La contraseña debe contener al menos una letra mayúscula.')
        ),
        RegexValidator(
            regex=r'^(?=.*[a-z])',  # Al menos una letra minúscula
            message=('La contraseña debe contener al menos una letra minúscula.')
        ),
        RegexValidator(
            regex=r'^(?=.*\d)',  # Al menos un dígito
            message=('La contraseña debe contener al menos un dígito.')
        ),
        RegexValidator(
            regex=r'^(?=.*[@$!%*?&])',  # Al menos un carácter especial
            message=('La contraseña debe contener al menos un carácter especial (@$!%*?&).')
        ),
        RegexValidator(
            regex=r'^.{8,}$',  # Al menos 8 caracteres de longitud
            message=('La contraseña debe tener al menos 8 caracteres de longitud.')
        )
    ])

    class Meta:
        model = Profile
        fields = ['username', 'password', 'email', 'bio']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(ProfileCreationSerializer, self).create(validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        # Añadir claims personalizados
        data['username'] = self.user.username
        return data

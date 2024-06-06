from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Profile

class ProfileCrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'emil', 'bio']

    def create(self, validated_data):
        validated_data["password"] = serializers.CharField(write_only=True, required=True, validators=[
                RegexValidator(
                    regex=r'^(?=.*[A-Z])',  # Al menos una letra mayúscula
                    message=('The password must contain at least one uppercase letter.')
                ),
                RegexValidator(
                    regex=r'^(?=.*[a-z])',  # Al menos una letra minúscula
                    message=('The password must contain at least one lowercase letter.')
                ),
                RegexValidator(
                    regex=r'^(?=.*\d)',  # Al menos un dígito
                    message=('The password must contain at least one digit.')
                ),
                RegexValidator(
                    regex=r'^(?=.[@$!%?&])',  # Al menos un carácter especial
                    message=('The password must contain at least one special character (@$!%*?&).')
                ),
                RegexValidator(
                    regex=r'^.{8,}$',  # Al menos 8 caracteres de longitud
                    message=('The password must be at least 8 characters long.')
                )
            ])
        validated_data['password'] = make_password(validated_data.get ( 'password'))
        return super(ProfileCrationSerializer, self).create(validated_data)
    
        
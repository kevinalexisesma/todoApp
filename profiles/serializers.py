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
                    regex=r'^(?=.*[A-Z])',  # At least one capital letter
                    message=('The password must contain at least one uppercase letter.')
                ),
                RegexValidator(
                    regex=r'^(?=.*[a-z])',  # At least one lowercase letter
                    message=('The password must contain at least one lowercase letter.')
                ),
                RegexValidator(
                    regex=r'^(?=.*\d)',  # At least one digit
                    message=('The password must contain at least one digit.')
                ),
                RegexValidator(
                    regex=r'^(?=.[@$!%?&])',  # At least one special character
                    message=('The password must contain at least one special character (@$!%*?&).')
                ),
                RegexValidator(
                    regex=r'^.{8,}$',  # At least 8 characters long
                    message=('The password must be at least 8 characters long.')
                )
            ])
        validated_data['password'] = make_password(validated_data.get ( 'password'))
        return super(ProfileCrationSerializer, self).create(validated_data)
    
        
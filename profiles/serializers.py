from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Profile

class ProfileCrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'emil', 'bio']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(ProfileCrationSerializer, self).create(validated_data)
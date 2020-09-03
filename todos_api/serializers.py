from rest_framework import serializers
from .models import Todos,UserProfile


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todos
        fields = ('id', 'user', 'name', 'isCompleted', 'created_on')
        extra_kwargs = {
            'user': {'read_only': True}
        }


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'avatar',  'password')
        extra_kwargs = {
            'password': {
                 'write_only': True,
                 'style': {'input_type': 'password'}
        }
        }

    def create(self, validated_data):

        user = UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            avatar = validated_data['avatar'],
            password = validated_data['password']
        )

        return user


from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'image': {'required': False, 'allow_null': True},
        }


 
class AddProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddProject
        fields = '__all__'

 
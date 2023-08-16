from rest_framework import serializers
from .models import User_data

class UserSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User_data
        fields = '__all__'

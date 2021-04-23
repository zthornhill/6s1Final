from rest_framework import serializers
from .models import Subscription, CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        print("VALIDATED DATA")
        print(validated_data)
        customuser = CustomUser.objects.create_user(
            validated_data['username'],
            customusername=validated_data['customusername'],
            password=validated_data['password'],
            phone=validated_data['phone'],
            address=validated_data['address'],
            city=validated_data['city'],
            country=validated_data['country']
        )
        return customuser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('pk', 'name', 'description', 'price', 'start_date', 'end_date')

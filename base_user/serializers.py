from rest_framework import serializers
from .models import CustomUser, UserProfile
from multimedia_manager.serializers import MediaFileSerializer, DocumentFileSerializer
from django.contrib.auth.models import Group
from rest_framework.response import Response
import re

class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializador para el perfil de usuario
    """
    foto = MediaFileSerializer(read_only=True)
    usuario_pdf = DocumentFileSerializer(read_only=True)
    profesion = serializers.CharField(
        source='get_profesion',
        read_only=True
    )
    
    class Meta:
        model = UserProfile
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'password2', 'email')
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def validate_email(self, value):
        REGEX_EMAIL = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(REGEX_EMAIL, value):
            raise serializers.ValidationError("El email no tiene un formato válido.")
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email ya existe.")
        return value

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("El nombre de usuario ya existe.")
        return value

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password2": "Las contraseñas no coinciden."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        # seleccionar el grupo de permisos según el rol(es el grupo de guest)
        guest_group = Group.objects.get(name='Guest')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            role='guest',
            is_active=True,
            is_staff=True,
        )
        return user

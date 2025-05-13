from rest_framework import serializers
from .models import CustomUser, UserProfile
from multimedia_manager.serializers import MediaFileSerializer, DocumentFileSerializer
from rest_framework.response import Response

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
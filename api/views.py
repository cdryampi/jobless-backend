from base_user.serializers import UserProfileSerializer, CustomUserSerializer
from base_user.models import UserProfile, CustomUser
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

class UserProfilesViewSet(viewsets.ViewSet):
    """
    API endpoint para listar perfiles de usuario.
    Solo permite listar perfiles, la gestión completa se realiza mediante el dashboard de Django.
    """
    
    def retrieve(self, request, pk=None):
        """
        Retorna un perfil de usuario específico.
        
        Parámetros:
        - uuid: ID del perfil a obtener (obligatorio)
        
        Respuestas:
        - 200: Perfil encontrado
        - 404: Perfil no encontrado
        """
        profile = get_object_or_404(UserProfile, uuid=pk)
        return Response(UserProfileSerializer(profile).data)
    
    def list(self, request):
        """
        Retorna una lista paginada de perfiles de usuario.
        
        Parámetros:
        - page: Número de página (opcional, por defecto 1)
        - page_size: Tamaño de página (opcional, por defecto 10)
        """
        try:
            # Obtener parámetros de paginación
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 10))
            
            # Obtener todos los perfiles ordenados por nombre ascendente
            profiles = UserProfile.objects.all().order_by('nombre')
            
            # Crear paginador
            paginator = Paginator(profiles, page_size)
            
            # Obtener la página solicitada
            page_profiles = paginator.get_page(page)
            
            # Serializar los perfiles
            serializer = UserProfileSerializer(page_profiles.object_list, many=True)
            
            # Preparar respuesta con paginación
            response_data = {
                'count': paginator.count,
                'num_pages': paginator.num_pages,
                'current_page': page,
                'results': serializer.data
            }
            
            return Response(response_data)
            
        except Exception as e:
            return Response(
                {'error': f'Error al obtener la lista de perfiles: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
    @action(detail=False, methods=['get'])
    def list_all(self, request, *args, **kwargs):
        """
        Retorna todos los perfiles de usuario sin paginación.
        
        ADVERTENCIA: Esta endpoint podría ser lenta con muchos registros.
        """
        try:
            profiles = UserProfile.objects.all()
            serializer = UserProfileSerializer(profiles, many=True)
            return Response(serializer.data)
            
        except Exception as e:
            return Response(
                {'error': f'Error al obtener todos los perfiles: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class CustomUserView(generics.CreateAPIView):
    """
    API endpoint para registrar nuevos usuarios.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        """
        Crea un nuevo usuario con validación completa.
        Devuelve también el token de autenticación.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            "user": CustomUserSerializer(user).data,
            "token": token.key,
        }, status=status.HTTP_201_CREATED)
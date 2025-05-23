from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserProfilesViewSet, CustomUserView

# Crear router para los viewsets
router = DefaultRouter()
router.register(r'userprofiles', UserProfilesViewSet, basename='userprofile')

# URLs de la aplicación
urlpatterns = [
    # Ruta personalizada para registrar usuarios
    path('register/', CustomUserView.as_view(), name='customuser-register'),
    
    # Incluir las URLs generadas por el router
    *router.urls,
]

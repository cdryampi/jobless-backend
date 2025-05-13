from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserProfilesViewSet

# Crear router para los viewsets
router = DefaultRouter()

# Registrar los viewsets
router.register(r'userprofiles', UserProfilesViewSet, basename='userprofile')

# URLs de la aplicación
urlpatterns = [
    # Incluir las URLs generadas por el router
    *router.urls,
]

from django.apps import AppConfig


class BaseUserConfig(AppConfig):
    """
    Configuración de la aplicación base_user
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_user'
    def ready(self):
        import base_user.signals
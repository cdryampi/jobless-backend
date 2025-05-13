from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from .models import CustomUser, UserProfile
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Crea o actualiza el perfil de usuario más la configuración de correo y asigna grupos y permisos basados en el rol.
    """
    # Crear perfil si no existe
    if created:
        # Create a new UserProfile instance
        profile = UserProfile(user=instance)
        profile.save()

        # Asignar grupos basados en el rol del usuario
        if instance.role == 'admin':
            # Crear o recuperar el grupo "Admin"
            admin_group, _ = Group.objects.get_or_create(name='Admin')
            # Asignar el grupo al usuario
            instance.groups.add(admin_group)
            # Asignar todos los permisos del grupo al usuario
            for perm in admin_group.permissions.all():
                instance.user_permissions.add(perm)
        elif instance.role == 'guest':
            # Crear o recuperar el grupo "Guest"
            guest_group, _ = Group.objects.get_or_create(name='Guest')
            # Asignar el grupo al usuario
            instance.groups.add(guest_group)
            # Asignar permisos básicos al grupo
            basic_perms = Permission.objects.filter(codename__in=['view_customuser', 'view_userprofile'])
            guest_group.permissions.set(basic_perms)

@receiver(post_save, sender=CustomUser)
def create_auth_token(sender, instance, created, **kwargs):
    """
    Crea un token de autenticación para el usuario.
    """
    if created:
        Token.objects.create(user=instance)
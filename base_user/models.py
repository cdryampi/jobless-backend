from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    """
    Modelo de usuario personalizado
    """
    ROLES = (
        ('admin', 'Admin'),
        ('guest', 'Guest'),
        ('test', 'Test'),
    )
    role = models.CharField(
        max_length=10,
        choices=ROLES,
        default='guest'
    )
    profile_image = models.ForeignKey(
        'multimedia_manager.MediaFile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='profile_image',
        verbose_name='Imagen de perfil',
        help_text='Imagen de perfil del usuario',
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']

class UserProfile(models.Model):
    """
    Modelo que representa a un usuario y sus datos adicionales
    """
    PROFESIONES = (
        ('estudiante', 'Estudiante'),
        ('profesor', 'Profesor'),
        ('trabajador', 'Trabajador'),
        ('desempleado', 'Desempleado'),
    )
    nombre = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Nombre',
        help_text='Nombre del usuario',
    )
    apellido = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Apellido',
        help_text='Apellido del usuario',
    )
    correo_electronico = models.EmailField(
        blank=True,
        null=True,
        verbose_name='Correo electrónico',
        help_text='Correo electrónico del usuario',
        unique=True,
    )
    resumen_habilidades = CKEditor5Field(
        verbose_name='Resumen de habilidades',
        help_text='Resumen de habilidades del usuario',
        null=True,
        blank=True,
        config_name='default',
    )
    descripcion = CKEditor5Field(
        verbose_name='Descripción',
        help_text='Descripción del usuario',
        null=True,
        blank=True,
        config_name='default',
    )
    profesion = models.CharField(
        max_length=100,
        choices=PROFESIONES,
        default='estudiante',
        verbose_name='Profesión',
        help_text='Profesión del usuario',
    )
    ciudad = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Ciudad',
        help_text='Ciudad del usuario',
    )
    edad = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Edad',
        help_text='Edad del usuario',
    )
    disponibilidad = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Disponibilidad',
        help_text='Disponibilidad del usuario',
    )
    usuario_pdf = models.ForeignKey(
        'multimedia_manager.DocumentFile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='usuario_pdf',
        verbose_name='Usuario PDF',
        help_text='Usuario PDF del usuario',
    )
    foto = models.ForeignKey(
        'multimedia_manager.MediaFile',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_profile_foto',
        verbose_name='Foto',
        help_text='Foto del usuario',
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_profile',
        verbose_name='Usuario',
        help_text='Usuario del perfil',
    )

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
    @property
    def get_profesion(self):
        profesiones_dict = dict(self.PROFESIONES)
        return profesiones_dict.get(self.profesion, 'Aún no tiene profesión')
    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(user_id=1)
        return obj
    def __str__(self):
        return self.nombre_completo
    class Meta:
        verbose_name = 'Perfil de usuario'
        verbose_name_plural = 'Perfiles de usuario'
        ordering = ['user']
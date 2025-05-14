from django.core.management.base import BaseCommand
from base_user.models import CustomUser, UserProfile
import json
from pathlib import Path
from multimedia_manager.models import MediaFile, DocumentFile
from django.core.files import File

base_path = Path(__file__).resolve().parent
fixtures_path = base_path / "fixtures"
img_url = fixtures_path / "sample.jpg"
pdf_url = fixtures_path / "sample.pdf"

class Command(BaseCommand):
    help = 'Crea el superusuario y varios usuarios con perfiles desde JSON'

    def handle(self, *args, **options):
        base_path = Path(__file__).resolve().parent
        json_path = base_path / "initial_profiles.json"
        self.stdout.write(
            self.style.SUCCESS(f"Eliminando todos los datos de la Base de Datos")
        )
        CustomUser.objects.all().delete()
        UserProfile.objects.all().delete()
        MediaFile.objects.all().delete()
        DocumentFile.objects.all().delete()
        self.stdout.write(
            self.style.SUCCESS(f"Todos los datos de la Base de Datos han sido eliminados")
        )
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                perfiles = json.load(f)
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"❌ Archivo JSON no encontrado en {json_path}"))
            return

        for username, profile_data in perfiles.items():
            user, created = CustomUser.objects.get_or_create(
                username=username,
                defaults={
                    'email': f'{username}@example.com',
                    'is_staff': username in ['admin', 'staff'],
                    'is_superuser': username == 'admin',
                }
            )

            if created:
                user.set_password(f'{username}123')
                user.save()
                self.stdout.write(self.style.SUCCESS(f'✅ Usuario creado: {username} / {username}123'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️ Usuario ya existía: {username}'))

            profile, p_created = UserProfile.objects.get_or_create(
                user=user,
                defaults={
                    'nombre': profile_data.get('nombre', ''),
                    'apellido': profile_data.get('apellido', ''),
                    'correo_electronico': user.email,
                    'profesion': profile_data.get('profesion', 'estudiante'),
                    'ciudad': profile_data.get('ciudad', ''),
                    'edad': profile_data.get('edad', 0),
                    'disponibilidad': profile_data.get('disponibilidad', ''),
                    'resumen_habilidades': profile_data.get('resumen_habilidades', ''),
                    'descripcion': profile_data.get('descripcion', ''),
                }
            )

            if profile:
                with open(img_url, 'rb') as img_file:
                    foto = MediaFile.objects.create(file=File(img_file, name="sample image"), title="sample image", creado_por=user)
                
                with open(pdf_url, 'rb') as pdf_file:
                    cv = DocumentFile.objects.create(file=File(pdf_file, name="sample pdf"), title="sample pdf", creado_por=user)
                
                profile.foto = foto
                profile.usuario_pdf = cv
                profile.nombre = profile_data.get('nombre', '')
                profile.apellido = profile_data.get('apellido', '')
                profile.correo_electronico = user.email
                profile.profesion = profile_data.get('profesion', 'estudiante')
                profile.ciudad = profile_data.get('ciudad', '')
                profile.edad = profile_data.get('edad', 0)
                profile.disponibilidad = profile_data.get('disponibilidad', '')
                profile.resumen_habilidades = profile_data.get('resumen_habilidades', '')
                profile.descripcion = profile_data.get('descripcion', '')

                profile.save()
                self.stdout.write(self.style.SUCCESS(f'🧾 Perfil actualizado para {username}'))
            else:
                self.stdout.write(self.style.WARNING(f'🧾 Perfil creado para {username}'))

        self.stdout.write(self.style.SUCCESS('🎉 Usuarios y perfiles iniciales generados.'))

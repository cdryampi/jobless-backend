from django.core.management.base import BaseCommand
from base_user.models import CustomUser, UserProfile
import json
from pathlib import Path
from multimedia_manager.models import MediaFile, DocumentFile
from django.core.files import File
from django.core.management import call_command

base_path = Path(__file__).resolve().parent
fixtures_path = base_path / "fixtures"
img_url = fixtures_path / "sample.jpg"
pdf_url = fixtures_path / "sample.pdf"

class Command(BaseCommand):
    help = 'Crea el superusuario y varios usuarios con perfiles desde JSON'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(f"Eliminando todos los datos de la Base de Datos")
        )
        call_command('seed_delete')
        self.stdout.write(
            self.style.SUCCESS(f"Creando grupos y sus permisos")
        )
        call_command('seed_permissions')
        call_command('create_groups')
        call_command('seed_sample_data')


        self.stdout.write(self.style.SUCCESS('🎉 Usuarios y perfiles iniciales generados.'))

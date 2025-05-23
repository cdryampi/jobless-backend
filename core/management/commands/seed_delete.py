from django.core.management.base import BaseCommand
from base_user.models import CustomUser, UserProfile
from multimedia_manager.models import MediaFile, DocumentFile
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Crea el superusuario y varios usuarios con perfiles desde JSON'

    def handle(self, *args, **options):
        """
        Elimina todos los datos de la base de datos.
        """
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
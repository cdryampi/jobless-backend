from django.core.management.base import BaseCommand
from django.apps import apps
from django.contrib.auth.management import create_permissions

class Command(BaseCommand):
    help = "Fuerza la creación de todos los permisos por modelo (útil después de nuevas migraciones)."

    def handle(self, *args, **kwargs):
        for app_config in apps.get_app_configs():
            try:
                create_permissions(app_config, verbosity=0)
                self.stdout.write(self.style.SUCCESS(f"✔ Permisos creados para la app '{app_config.label}'"))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"⚠️  Error creando permisos para '{app_config.label}': {e}"))

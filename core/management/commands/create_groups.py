from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = "Crea los grupos 'Admin' y 'Guest' con permisos específicos"

    def handle(self, *args, **options):
        modelos_limitados = ['customuser', 'userprofile']
        modelos_completos = ['mediafile', 'documentfile']
        permisos_limitados = ['view', 'change']
        permisos_completos = ['add', 'change', 'delete', 'view']

        # Grupo Admin: todos los permisos
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        all_perms = Permission.objects.all()
        admin_group.permissions.set(all_perms)
        self.stdout.write(self.style.SUCCESS("✔ Grupo 'Admin' configurado con todos los permisos."))

        # Grupo Guest: permisos personalizados
        guest_group, _ = Group.objects.get_or_create(name='Guest')

        codename_guest = [
            f"{perm}_{model}"
            for model in modelos_limitados
            for perm in permisos_limitados
        ] + [
            f"{perm}_{model}"
            for model in modelos_completos
            for perm in permisos_completos
        ]

        guest_perms = Permission.objects.filter(codename__in=codename_guest)
        guest_group.permissions.set(guest_perms)
        self.stdout.write(self.style.SUCCESS("✔ Grupo 'Guest' configurado con permisos limitados y CRUD para multimedia."))

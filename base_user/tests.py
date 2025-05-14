from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import UserProfile
from pathlib import Path
from multimedia_manager.models import MediaFile, DocumentFile
from django.core.files import File

base_path = Path(__file__).resolve().parent.parent # raiz del proyecto jobless-backend
fixtures_path = base_path / "core" / "management" / "commands" / "fixtures"
img_url = fixtures_path / "sample.jpg"
pdf_url = fixtures_path / "sample.pdf"

User = get_user_model()

class UserTokenTest(TestCase):

    def test_token_is_created_for_new_user(self):
        """
        Verifica que al crear un usuario, se genere automáticamente un token de autenticación.
        """
        user = User.objects.create_user(username="testuser", password="testpassword")

        token = Token.objects.get(user=user) # recuperar el token del usuario, en teoría debería existir porque el signal lo crea automáticamente.

        self.assertIsNotNone(token)
        print(f"✔ Token generado correctamente: {token.key}")

    def test_profile_is_created_for_new_user(self):
        """
        Verifica que al crear un usuario, su perfil también se cree automáticamente.
        """
        user = User.objects.create_user(username="testuser2", password="testpassword")
        profile = UserProfile.objects.get(user=user)

        self.assertIsNotNone(profile)
        print(f"✔ Perfil generado correctamente para {user.username}")

    def test_mediafile_is_created_for_new_user(self):
        """
        Verifica que al crear un usuario, su perfil también se cree automáticamente.
        """
        import uuid
        user = User.objects.create_user(username=f"testuser2_{uuid.uuid4().hex}", password="testpassword")
        profile = UserProfile.objects.get(user=user)
        with open(img_url, 'rb') as img_file:
            media = MediaFile.objects.create(file=File(img_file, name="test media"), title="test media")
        media.creado_por = user
        media.save()
        profile.foto = media
        profile.save()

        self.assertIsNotNone(profile.foto)
        print(f"✔ MediaFile generado correctamente para {user.username}")
    
    def test_documentfile_is_created_for_new_user(self):
        """
        Verifica que al crear un usuario, su perfil también se cree automáticamente.
        """
        user = User.objects.create_user(username="testuser2", password="testpassword")
        profile = UserProfile.objects.get(user=user)
        with open(pdf_url, 'rb') as pdf_file:
            document = DocumentFile.objects.create(file=File(pdf_file, name="test document"), title="test document")
        document.creado_por = user
        document.save()
        profile.usuario_pdf = document
        profile.save()

        self.assertIsNotNone(profile.usuario_pdf)
        print(f"✔ DocumentFile generado correctamente para {user.username}")
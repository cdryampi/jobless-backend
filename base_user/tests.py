from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import UserProfile
from pathlib import Path
from multimedia_manager.models import MediaFile, DocumentFile
from django.core.files import File
from rest_framework.test import APIClient
from django.contrib.auth.models import Group



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

class UserAuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Crear el grupo de Guest necesario para la prueba o no funcionará porque el serializer lo asigna automáticamente al usuario.
        # Esto es necesario porque el signal de creación de usuario asigna grupos automáticamente.
        # Si el grupo ya existe, no se creará de nuevo.
        self.guest_group, _ = Group.objects.get_or_create(name='Guest')
        self.guest_group.permissions.set(Group.objects.get(name='Guest').permissions.all())
        self.guest_group.save()

        # Crear un usuario de prueba
        self.user = User.objects.create_user(
            username="uuiduser",
            password="123456",
            email="uuiduser@example.com"
        )
        self.token = Token.objects.get(user=self.user)
        self.profile = self.user.user_profile  # creado por signal
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_registro_usuario_y_creacion_perfil(self):
        """
        Verifica que al registrar un usuario se cree perfil y token automáticamente.
        """
        data = {
            "username": "usuario_guest",
            "email": "guest@example.com",
            "password": "test1234",
            "password2": "test1234"
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, 201)

        user = User.objects.get(username="usuario_guest")
        self.assertTrue(UserProfile.objects.filter(user=user).exists())

        token = Token.objects.get(user=user)
        self.assertIsNotNone(token.key)

    def test_obtener_perfil_por_uuid(self):
        """
        Verifica que se puede acceder al perfil de usuario vía su UUID.
        """
        url = f'/api/userprofiles/{self.profile.uuid}/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['uuid'], str(self.profile.uuid))
        self.assertEqual(response.data['user'], self.user.id)
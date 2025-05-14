import uuid
from base_user.models import UserProfile

def generate_uuid()->str:
    """
    Genera un UUID aleatorio
    """
    return str(uuid.uuid4())

def regenerar_los_uuids_perfiles()->None:
    
    perfiles = UserProfile.objects.all()
    for perfil in perfiles:
        perfil.uuid = generate_uuid()
        perfil.save()
    print("✅ UUIDs regenerados para todos los perfiles")
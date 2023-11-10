from rest_framework.exceptions import AuthenticationFailed
from google.oauth2.id_token import verify_oauth2_token
from google.auth import transport as google_transport

from api.management.serializers import GoogleAuthSerializer
from management.models import AuthUser
from svs import settings
from . import base_auth


def check_google_auth(google_user) -> dict:
    try:
        verify_oauth2_token(
            google_user['token'], google_transport.Request(), settings.GOOGLE_CLIENT_ID
        )
    except ValueError:
        raise AuthenticationFailed(code=403, detail='Bad token Google')

    user, _ = AuthUser.objects.get_or_create(
        email=google_user['email'],
        display_name=google_user['display_name']
    )
    return base_auth.create_token(user.id)

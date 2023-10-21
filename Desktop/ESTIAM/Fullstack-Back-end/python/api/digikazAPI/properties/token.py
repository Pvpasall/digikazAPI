from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token


class MyTokenObtainPairSerializer(TokenObtainPairSerializer) :
    def get_token(cls, user) :
        token = super().get_token(user)

        token['isAdmin'] = user.is_superuser

        return token
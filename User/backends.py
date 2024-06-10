from django.contrib.auth.backends import BaseBackend
from User.models import Eleve, Enseignant
from django.contrib.auth.hashers import check_password

class CustomBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = Eleve.objects.get(email=email)
        except Eleve.DoesNotExist:
            try:
                user = Enseignant.objects.get(email=email)
            except Enseignant.DoesNotExist:
                return None

        if user and check_password(password, user.password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Eleve.objects.get(pk=user_id)
        except Eleve.DoesNotExist:
            try:
                return Enseignant.objects.get(pk=user_id)
            except Enseignant.DoesNotExist:
                return None

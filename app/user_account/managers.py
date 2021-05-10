from django.contrib.auth.models import BaseUserManager
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text


class UserAccountManager(BaseUserManager):
    """ Custom manager for the User Model"""

    def create_user(self, email, password=None, **extra_fields):
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user

    def get_object_or_none(self, *args, **kwargs):
        try:
            return self.model.objects.get(*args, **kwargs)
        except:
            return None

    def get_object_by_uidb64(self, uidb64):
        user = None
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = self.get_object_or_none(id=id)
        except:
            user = None

        return user

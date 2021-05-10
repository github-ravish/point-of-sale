import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    """
    Create a superuser if none exist
    Example:
        manage.py createsuperuser_if_none_exists
    """

    def handle(self, *args, **options):

        user = get_user_model()
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        if user.objects.get_object_or_none(email=email):
            self.stdout.write(f'Super user "{email}" already exists')
            return


        user.objects.create_superuser(password=password, email=email)

        self.stdout.write(f'Super user "{email}" was created')
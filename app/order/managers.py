from django.db.models import Manager


class CustomManager(Manager):
    """ Custom manager for the User Model"""

    def get_object_or_none(self, *args, **kwargs):
        try:
            return self.model.objects.get(*args, **kwargs)
        except:
            return None

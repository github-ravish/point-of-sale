from django.db.models import Manager


class ActiveShopManager(Manager):
    """ Custom manager for the User Model"""

    def get_object_or_none(self, *args, **kwargs):
        try:
            return self.model.objects.get(is_active=True, *args, **kwargs)
        except:
            return None


class CustomManager(Manager):

    def get_queryset(self):
        return super().get_queryset().filter(
            is_active=True,
        )

    def get_object_or_none(self, *args, **kwargs):
        try:
            return self.model.objects.get(
                *args,
                **kwargs
            )
        except:
            return None

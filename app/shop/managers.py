from django.db.models import Manager


class ActiveShopManager(Manager):
    """ Custom manager for the User Model"""

    def get_object_or_none(self, *args, **kwargs):
        try:
            return self.model.objects.get(is_active=True, *args, **kwargs)
        except:
            return None


class OwnerShopManager(Manager):

    def get_object_or_none(self, *args, **kwargs):
        try:
            return self.model.objects.get(
                is_active=True,
                shop_staff__role=2,
                *args,
                **kwargs
            )
        except:
            return None


class POSShopManager(Manager):

    def get_object_or_none(self, *args, **kwargs):
        try:
            return self.model.objects.get(
                is_active=True,
                shop_staff__role=4,
                *args,
                **kwargs
            )
        except:
            return None

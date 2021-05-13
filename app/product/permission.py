from django.core.exceptions import PermissionDenied

from shop.models.shop import Shop
from utils.uuid import is_valid_uuid


class RoleRequiredMixin(object):

    roles_required = None

    def dispatch(self, request, *args, **kwargs):
        shop_slug = self.kwargs.get("shop_slug")
        if not request.user.is_authenticated:
            raise PermissionDenied
        else:
            if self.roles_required:
                if not is_valid_uuid(shop_slug):
                    raise PermissionDenied
                if not Shop.custom_manager.filter(
                    shop_staff__user_account=request.user,
                    shop_staff__role__in=self.roles_required,
                    slug=shop_slug
                ).exists():
                    raise PermissionDenied
        return super(RoleRequiredMixin, self).dispatch(request, *args, **kwargs)

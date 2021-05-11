from django.core.exceptions import PermissionDenied

from shop.models.shop import Shop


class RoleRequiredMixin(object):

    roles_required = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        else:
            if self.roles_required:
                if not Shop.custom_manager.filter(
                    shop_staff__user_account=request.user,
                    shop_staff__role__in=self.roles_required
                ).exists():
                    raise PermissionDenied
        return super(RoleRequiredMixin, self).dispatch(request, *args, **kwargs)

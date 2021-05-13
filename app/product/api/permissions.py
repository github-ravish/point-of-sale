from rest_framework import permissions


class ProductManagePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        shop_slug = view.kwargs.get('shop_slug')
        if request.user.user_shop.filter(
            role__in=view.roles_allowed,
            related_shop__slug=shop_slug
        ).exists() and request.user.is_authenticated:
            return True
        else:
            return False

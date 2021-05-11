from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='has_shop_role')
def has_shop_role(user, roles):
    if not user.is_authenticated:
        return False
    roles = list(roles.split(','))
    user_role = []
    for role in roles:
        user_role.append(settings.SHOP_ROLE_CHOICE_REVERSE.get(role))

    if user.user_shop.filter(role__in=user_role).exists():
        return True
    else:
        return False

from django.forms import ModelForm
from django.conf import settings

from .models.shop import Shop
from shop.models.shop_staff import ShopStaff


class ShopModelForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(ShopModelForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        shop = super(ShopModelForm, self).save(commit=True)
        staff, created = ShopStaff.objects.get_or_create(
            user_account=self.user,
            role=settings.SHOP_ROLE_CHOICE_REVERSE.get('SHOP_OWNER')
        )
        shop.shop_staff.add(staff)
        shop.save()
        return shop

    class Meta:
        model = Shop
        fields = ('name', 'country', 'state', 'city', 'area', 'pincode',)

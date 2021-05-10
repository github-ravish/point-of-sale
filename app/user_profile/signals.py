from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
import datetime


from user_account.signals import user_created
from .models import UserProfile


@receiver(user_created)
def create_profile(sender, **kwargs):
    referred_by = None
    if kwargs["referral_code"] != None:
        try:
            id = force_text(
                urlsafe_base64_decode(kwargs["refferal_code"]))
            referred_by = get_user_model().objects.get_object_or_none(id=id)
        except:
            referred_by = None
    UserProfile.objects.create(
        user_account=kwargs["user"], referred_by=referred_by)
